def cpath():
    def get_int(prompt):
        while True:
            try:
                n = int(input(prompt))
                return n if n > 0 else print("Must be positive.")
            except: print("Invalid input.")

    def get_activity(i, n, a):
        while True:
            name = input(f"Act {i+1} Name: ")
            if name in a[:i]:
                print(f"Error: {name} exists. Retry.")
                continue
            duration = get_int("Duration: ")
            pred = input("Pred(0=none): ")
            pred_list = [] if pred == "0" else [a.index(p.strip()) for p in pred.split(",") if p.strip() in a[:i]]
            if len(pred_list) == len(pred.split(",")) - (1 if pred == "0" else 0):
                return name, duration, pred_list
            print(f"Invalid pred. Retry Act {i+1}.")

    def calc_times(durations):
        es = [0] * n
        ef = [0] * n
        for i in range(n):
            es[i] = max([ef[j] for j in p[i]] + [0])
            ef[i] = es[i] + durations[i]
        mt = max(ef)
        ls = [mt] * n
        lf = [mt] * n
        for i in range(n-1, -1, -1):
            successors = [j for j in range(n) if i in p[j]]
            lf[i] = min([ls[j] for j in successors] + [mt])
            ls[i] = lf[i] - durations[i]
        return es, ef, ls, lf, mt

    def find_critical(es, ls):
        paths, stack = [], [(i, [i]) for i in range(n) if not p[i]]
        while stack:
            node, path = stack.pop()
            if not any(node in p[i] for i in range(n)):
                paths.append(path)
            else:
                stack.extend((i, path + [i]) for i in range(n) if node in p[i] and ls[i] - es[i] == 0)
        return [path for path in paths if all(ls[i] - es[i] == 0 for i in path)]

    def crash_project(d, crash_used, target=None, manual=True):
        es, ef, ls, lf, mt = calc_times(d)
        if target and mt <= target:
            return d, crash_used, 0, 0

        best_d, best_crash, best_cost, best_mt = d[:], crash_used[:], float('inf'), mt

        def try_crash():
            nonlocal best_d, best_crash, best_cost, best_mt
            queue = [(d[:], crash_used[:], 0)]
            while queue:
                current_d, current_crash, current_cost = queue.pop(0)
                es, ef, ls, lf, mt = calc_times(current_d)
                if (not target or mt <= target) and current_cost < best_cost:
                    best_d, best_crash, best_cost, best_mt = current_d, current_crash, current_cost, mt
                    if target and mt <= target:
                        return True
                if current_cost >= best_cost:
                    continue
                for i in range(n):
                    if ls[i] - es[i] == 0 and current_d[i] > 1 and (crash_limit[i] == 0 or current_crash[i] < crash_limit[i]):
                        new_d, new_crash = current_d[:], current_crash[:]
                        new_d[i] -= 1
                        new_crash[i] += 1
                        queue.append((new_d, new_crash, current_cost + crash_cost[i]))
            return False

        if manual:
            while True:
                act_input = input("Activities to crash (or Enter): ")
                if not act_input:
                    break
                for idx in [a.index(act.strip()) for act in act_input.split(",") if act.strip() in a]:
                    if crash_limit[idx] == 0:
                        crash_limit[idx] = get_int(f"Set crash limit for {a[idx]}: ")
                    max_crash = min(d[idx]-1, crash_limit[idx]-crash_used[idx] if crash_limit[idx] > 0 else d[idx]-1)
                    if max_crash <= 0:
                        print(f"{a[idx]}: Cannot crash further")
                        continue
                    crash_days = get_int(f"Days to crash {a[idx]} (max {max_crash}): ")
                    crash_days = min(crash_days, max_crash)
                    d[idx] -= crash_days
                    crash_used[idx] += crash_days
                    print(f"{a[idx]}: Reduced to {d[idx]} days")
        else:
            print("Calculating optimal crashing...")
            solution_found = try_crash()
            if solution_found:
                print("Optimal crashing solution found.")
            else:
                print("No feasible crashing solution found to meet the target.")
            d, crash_used = best_d, best_crash

        return d, crash_used, sum(crash_cost[i] * crash_used[i] for i in range(n)), mt - calc_times(d)[4]

    # Main execution flow
    n = get_int("Num activities: ")
    a, d, p = [], [], []
    crash_cost, crash_limit, crash_used = [0]*n, [0]*n, [0]*n

    for i in range(n):
        name, duration, predecessors = get_activity(i, n, a)
        a.append(name), d.append(duration), p.append(predecessors)

    while True:
        es, ef, ls, lf, mt = calc_times(d)
        critical_paths = find_critical(es, ls)

        print(f"\nTotal Duration: {mt}")
        print("\nActivity Details:")
        for i in range(n):
            crash_info = f" (Crashed: {crash_used[i]}/{crash_limit[i]})" if crash_limit[i] > 0 else ""
            print(f"{a[i]}: ES={es[i]}, LS={ls[i]}, Slack={ls[i]-es[i]}{crash_info}")

        print("\nCritical Paths:")
        for idx, path in enumerate(critical_paths):
            print(f"Path {idx+1}: {' -> '.join(a[i] for i in path)}")
            print(f"Duration: {sum(d[i] for i in path)}")

        choice = input("\n1:Continue 2:Crash 3:CrashCost 4:End\nChoose option: ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            reduction_type = input("Reduce to (t) or by (b) days? (Enter for min): ").lower()
            target = get_int("Target duration: ") if reduction_type == 't' else (mt - get_int("Days to reduce: ") if reduction_type == 'b' else 1)
            d, crash_used, total_cost, time_saved = crash_project(d, crash_used, target)
            print(f"\nTime Reduced: {time_saved} days")
            print(f"Final Duration: {calc_times(d)[4]} days")
            print(f"Total Cost: ${total_cost}")
        elif choice == "3":
            reduction_type = input("Reduce to (t) or by (b) days? (Enter for min): ").lower()
            target = get_int("Target duration: ") if reduction_type == 't' else (mt - get_int("Days to reduce: ") if reduction_type == 'b' else 1)
            while True:
                act_input = input("Activities for crash cost (or Enter): ")
                if not act_input:
                    break
                cost = get_int("Cost per day for all: ")
                for idx in [a.index(act.strip()) for act in act_input.split(",") if act.strip() in a]:
                    crash_cost[idx] = cost
                    crash_limit[idx] = get_int(f"Set crash limit for {a[idx]}: ")
                    print(f"{a[idx]}: Cost set to ${cost}/day, limit set to {crash_limit[idx]} days")
            print("\nCalculating optimal crashing...")
            d, crash_used, total_cost, time_saved = crash_project(d, crash_used, target, manual=False)
            print(f"\nTime Reduced: {time_saved} days")
            print(f"Final Duration: {calc_times(d)[4]} days")
            print(f"Total Cost: ${total_cost}")
            print("\nActivities crashed:")
            for i in range(n):
                if crash_used[i] > 0:
                    print(f"{a[i]}: {crash_used[i]} days (Cost: ${crash_used[i] * crash_cost[i]})")
        elif choice == "4":
            break
        else:
            print("Invalid choice (1-4)")

# Run the program
cpath()