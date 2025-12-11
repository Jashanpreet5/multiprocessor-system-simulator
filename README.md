# multiprocessor-system-simulator

# 🪄Dynamic Load Balancing in Multiprocessor Systems
A lightweight, command-line-based simulator that demonstrates **dynamic load balancing** by distributing tasks across multiple processors in real time. It assigns each incoming task to the **least-loaded processor** at the moment of arrival, adapting dynamically to changing system loads.

Ideal for **Operating Systems coursework**, **distributed systems education**, and **performance analysis experiments**.

![Demo](https://img.shields.io/badge/Status-Working-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- Implements **Least-Loaded Processor Assignment** (dynamic load balancing)
- Supports multiple processors
- Random or manual task generation
- Tasks with variable CPU burst workloads
- Real-time load monitoring and adaptive assignment
- Detailed task assignment logs
- Final load distribution summary
- Fully CLI-driven (no GUI dependencies)
- Modular, clean code — easy to extend

## Project Structure
dynamic-load-balancer/
├── main.py              # Entry point with CLI interface
├── processor.py         # Processor class and load tracking
├── task.py              # Task model with workload
├── load_balancer.py     # Core dynamic balancing logic
├── utils.py             # Random task generator & helpers
├── requirements.txt     # (Optional) Dependencies
└── README.md            # This file

## Getting Started

### 1. Clone the Repository

'''bash
git clone https://github.com/your-username/dynamic-load-balancer.git
cd dynamic-load-balancer

2. Install Dependencies (if any)
pip install -r requirements.txt
Note: The simulator works with pure Python — requirements.txt is optional.

3. Run the Simulator
python3 main.py

You will be prompted to enter:
Number of processors
Number of tasks
Task generation mode (random or manual)

Example Interaction
=== Dynamic Load Balancing Simulator ===
Enter number of processors: 3
Enter number of tasks: 5
Generate tasks randomly? (y/n): y

Generated Task 1 with workload=7
Generated Task 2 with workload=2
Generated Task 3 with workload=9
Generated Task 4 with workload=3
Generated Task 5 with workload=5

Assigned Task 1 → CPU0
Assigned Task 2 → CPU1
Assigned Task 3 → CPU2
Assigned Task 4 → CPU1
Assigned Task 5 → CPU0

--- Final Load Distribution ---
CPU0 | Load=12 | Tasks=[1, 5]
CPU1 | Load=5  | Tasks=[2, 4]
CPU2 | Load=9  | Tasks=[3]

How It Works
  Concept                                              Description
Current Load                  Sum of workloads of all tasks currently assigned to a processor
Balancing Rule                New task is always assigned to the processor with the minimum current load
Adaptivity                    Decision is made at runtime using the latest system state

Educational Value
This simulator helps students understand:

Multiprocessor scheduling in Operating Systems
Dynamic vs Static load balancing
Real-time decision making in resource allocation
Importance of load monitoring
Fairness and performance optimization in distributed systems

Future Enhancements (Ideas)
Round Robin scheduling mode
Weighted load balancing (heterogeneous CPUs)
Task migration between processors
Real-time visualization (Matplotlib/Plotly)
Export results to CSV/JSON
Web interface using Streamlit
Task arrival times and queue simulation
Support for preemptive scheduling

License
This project is licensed under the MIT License — see the LICENSE file for details.

### Optional: Add a LICENSE file
Create a `LICENSE` file in the root with MIT License text (standard).

Let me know if you want me to generate:
- A PDF report version
- PowerPoint slides
- UML/class diagram
- Sample output screenshots

Happy coding and good luck with your submission! 🚀


