# CyberSecurity-Logger-Py

Project Overview

The Cybersecurity Logger is a simple Python application designed to log system events and analyze them for potential security breaches. This project demonstrates basic logging, error detection, and analysis capabilities, which are essential for monitoring system activities and ensuring security.

Features

Logs various types of events (INFO, WARNING, ERROR).
Analyzes log files to detect and highlight potential security issues.
Easy-to-read log format with timestamps and severity levels.
Installation

Clone the Repository:
bash
Copy code
git clone https://github.com/Lorenzofernz/CyberSecurity-Logger-Py.git
cd CyberSecurity-Logger-Py
Set Up the Virtual Environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Usage

Run the Logger:
bash
Copy code
python3 logger.py
Check the Logs:
Logs are saved in cybersecurity.log.
Analyze the Logs:
The application will print security alerts found in the log file.
Code Explanation

logger.py: Main script that sets up logging, logs events, and analyzes the log file.
log_event(event_type, message): Logs events based on their severity.
analyze_logs(): Reads the log file and highlights any ERROR events.
Contribution

Feel free to fork this repository, submit issues, and send pull requests to improve the project.
