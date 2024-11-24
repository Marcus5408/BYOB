import subprocess

# Start pyg.py
import sys
import os
import signal
pyg_process = subprocess.Popen([sys.executable, 'pyg.py'])

tk_part_process = subprocess.Popen([sys.executable, 'tk_part.py'])
tk_part_process = subprocess.Popen(['python', 'tk_part.py'])

# Wait for both processes to complete
pyg_process.wait()
tk_part_process.wait()
# Function to handle communication between processes
def communicate_between_processes():
    # Example: Send a signal from pyg_process to tk_part_process
    os.kill(tk_part_process.pid, signal.SIGUSR1)

# Register signal handler in tk_part.py to handle incoming signals
def signal_handler(signum, frame):
    print(f"Received signal: {signum}")

# Register the signal handler
signal.signal(signal.SIGUSR1, signal_handler)
