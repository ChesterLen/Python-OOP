class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if new_name == self.name:
            return "Name cannot be the same."
        
        self.name = new_name
        return self.name
    
    def change_due_date(self, new_date: str) -> str:
        if new_date == self.due_date:
            return "Date cannot be the same."
        
        self.due_date = new_date
        return self.due_date
    
    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if 0 < comment_number or comment_number > len(self.comments) - 1:
            return "Cannot find comment."
        
        self.comments[comment_number] = new_comment
        return ", ".join(self.comments)
    
    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"