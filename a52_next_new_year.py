# Next new year

from datetime import datetime

target_date = datetime(2026, 1, 1)

current_date = datetime.now()

# Calculate the time difference
time_left = target_date - current_date

print("Current date and time:", current_date)
print(f"Time left until 01.01.2026:\n{time_left}")
