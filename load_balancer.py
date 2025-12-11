from processor import Processor

class LoadBalancer:
    def __init__(self, num_processors):
        self.processors = [Processor(i) for i in range(num_processors)]

    def assign_task(self, task):
        # Dynamic load balancing: choose CPU with the lowest current load
        best_cpu = min(self.processors, key=lambda cpu: cpu.total_load)
        best_cpu.add_task(task)
        print(f"Assigned Task {task.tid} (load={task.workload}) → CPU{best_cpu.pid}")

    def show_distribution(self):
        print("\nProcessor Load Summary:\n")
        for cpu in self.processors:
            print(cpu)
