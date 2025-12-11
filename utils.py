import random
from task import Task

def create_random_tasks(n):
    tasks = []
    for i in range(1, n+1):
        workload = random.randint(1, 10)  # random workload units
        tasks.append(Task(i, workload))
        print(f"Generated Task {i} with workload={workload}")
    return tasks
