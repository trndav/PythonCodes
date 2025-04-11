# simple sleep
# import time

# def slow_task():
#     time.sleep(2)
#     print("Done")

# slow_task()
# slow_task()
# slow_task()


# import asyncio

# async def slow_task(name):
#     print(f"⏳ {name} started")
#     await asyncio.sleep(2)  # non-blocking wait
#     print(f"✅ {name} finished")

# async def main():
#     await asyncio.gather(
#         slow_task("Task 1"),
#         slow_task("Task 2"),
#         slow_task("Task 3")
#     )

# asyncio.run(main())

import asyncio
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("⏳ Timer started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"✅ Timer stopped. Elapsed time: {self.elapsed:.2f} seconds")

async def slow_task(name):
    print(f"🔄 {name} started")
    await asyncio.sleep(2)
    print(f"✅ {name} finished")

async def main():
    with Timer():
        await asyncio.gather(
            slow_task("Task 1"),
            slow_task("Task 2"),
            slow_task("Task 3")
        )

asyncio.run(main())
