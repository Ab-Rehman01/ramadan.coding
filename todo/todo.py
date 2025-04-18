import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from todo.json"""
    if not os.path.exists(TODO_FILE):
        return []  # Agar file nahi mili to empty list return karein
    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)  # JSON read karna
        except json.JSONDecodeError:
            return []  # Agar JSON corrupt hai to empty list

def save_tasks(tasks):
    """Save tasks to todo.json"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})  # ⬅️ Yeh line fix ki gayi hai
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command(name="list")
def list_tasks():

    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✔" if task['done'] else "✘"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int) 
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}") 

cli.add_command(add)
cli.add_command(list_tasks)  # Renamed to avoid conflict
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
