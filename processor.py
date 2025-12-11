class Processor:
    def __init__(self, pid):
        self.pid = pid
        self.tasks = []
        self.total_load = 0

    def add_task(self, task):
        self.tasks.append(task)
        self.total_load += task.workload

    def __repr__(self):
        return f"CPU{self.pid} | Load={self.total_load} | Tasks={[t.tid for t in self.tasks]}"
