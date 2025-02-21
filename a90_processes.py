import psutil
import time

start_time = time.time()
for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
    try:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, "
              f"CPU: {process.info['cpu_percent']}%, "
              f"Memory: {process.info['memory_info'].rss / (1024 * 1024):.2f} MB")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
end_time = time.time()

print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
print(f"Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB")
print("Execution Time:", end_time - start_time, "seconds")