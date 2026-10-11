def schedule_pipeline(tasks: list, resource_budget: int):
    current_time = 0
    available_resources = resource_budget
    completed = set()
    unscheduled = set(t['name'] for t in tasks)
    running = []
    schedule = []
    
   
    tasks_dict = {t['name']: t for t in tasks}

    while unscheduled or running:
        ended_this_step = [r for r in running if r[0] == current_time]
        running = [r for r in running if r[0] > current_time]
        
        for r in ended_this_step:
            completed.add(r[1])
            available_resources += r[2]
            
        ready_tasks = []
        for t_name in unscheduled:
            task = tasks_dict[t_name]
            if all(dep in completed for dep in task.get('depends_on', [])):
                ready_tasks.append(task)
            
        ready_tasks.sort(key=lambda x: x['name'])
        
        for task in ready_tasks:
            if task['resources'] <= available_resources:
                available_resources -= task['resources']
                unscheduled.remove(task['name'])
                running.append((current_time + task['duration'], task['name'], task['resources']))
                schedule.append({"task_name": task['name'], "start_time": current_time})
                
        if running:
            current_time = min(r[0] for r in running)
        else:
            break

    return sorted(schedule, key=lambda x: (x['start_time'], x['task_name']))