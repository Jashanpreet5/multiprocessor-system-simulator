from load_balancer import LoadBalancer
from task import Task
from utils import create_random_tasks

def main():
    print("\n=== Dynamic Load Balancing Simulator ===")

    num_processors = int(input("\nEnter number of processors: "))
    num_tasks = int(input("Enter number of tasks to generate: "))

    lb = LoadBalancer(num_processors)

    print("\nGenerating tasks...\n")
    tasks = create_random_tasks(num_tasks)

    print("Assigning tasks dynamically...\n")
    for task in tasks:
        lb.assign_task(task)

    print("\n--- Final Load Distribution ---")
    lb.show_distribution()

if __name__ == "__main__":
    main()
