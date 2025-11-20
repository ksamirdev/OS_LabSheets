# Task 4: VM Detection and Shell Interaction
# Create a shell script to print system details and a Python script to detect if the system is running inside a virtual machine.
#!/bin/bash
echo "Kernel Version:"
uname -r
echo "User:"
whoami
echo "Hardware Info:"
lscpu | grep 'Virtualization'