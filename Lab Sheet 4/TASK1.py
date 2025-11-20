# Task 1: Batch Processing Simulation (Python)
# Write a Python script to execute multiple .py files sequentially, mimicking batch processing.
import subprocess
scripts = ['script1.py', 'script2.py', 'script3.py']
for script in scripts:
    print(f"Executing {script}...")
    subprocess.call(['python3', script])