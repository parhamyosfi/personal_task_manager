
from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os

load_dotenv()

name = input("enter your name: ")
print(f"wellcome back {name}")

admin_mode = input("do you want to enter admin mode (yes/no)? ").lower()

if admin_mode == "yes":
    admin_password = input("please give me your admin password: ")
    if admin_password == os.getenv("ADMIN_CODE"):
        print("admin mode activated")
    else:
        print("wrong password")

tasks = load_tasks()

count = int(input("how many tasks do you want to add?: "))

for i in range(count):
    task_name = input("enter a task: ")
    priority = input("enter priority (low/mid/high): ").lower()

    task = {
        "name": task_name,
        "priority": priority
    }

    tasks.append(task)

save_tasks(tasks)
show_tasks(tasks)
