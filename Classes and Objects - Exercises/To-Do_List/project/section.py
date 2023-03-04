from typing import List
from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"
    
    def complete_task(self, task_name: str) -> str:
        task_to_complete = [t for t in self.tasks if t.name == task_name][0]

        if not task_to_complete:
            return f"Could not find task with the name {task_name}"
        
        task_to_complete.completed = True
        return f"Completed task {task_name}"
    
    def clean_section(self):
        cleared_tasks = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                cleared_tasks += 1
        
        return f"Cleared {cleared_tasks} tasks."
    
    def view_section(self):
        tasks_to_print = '\n'.join([task.details() for task in self.tasks])

        return f"Section {self.name}:\n" \
               f"{tasks_to_print}"