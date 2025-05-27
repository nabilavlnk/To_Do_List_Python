import csv

class Task:
    def __init__(self, task_name, due_date, status=False):
        self.task_name = task_name
        self.status = status
        self.due_date = due_date
    
    def change_name(self, new_name):
        self.task_name = new_name

    def change_due_date(self, new_date):
        self.due_date = new_date
    
    def status_marked(self):
        self.status = True
    
    def to_list(self):
        return [self.task_name, self.due_date, self.status]
    
class TaskManagement:
    def __init__(self):
        self.tasks = []
        self.from_csv()

    def save_to_csv(self):
        with open('data_to_do_list.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["task_name", "due_date", "status"]) # header
            for task in self.tasks:
                writer.writerow(task.to_list())
    
    def from_csv(self):
        try: 
            with open('C:\\Users\\valin\\To_Do_List_App\\data_to_do_list.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    task_name = row[0]
                    due_date = row[1]
                    status = True if row[2].strip().lower() == "true" else False
                    #print(f"DEBUG: row[2] = {row[2]} -> status = {status}")
                    task = Task(task_name, due_date, status)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

    def view_task(self):
        return self.tasks
        
    def add_task(self, task_name, due_date):
        new_task = Task(task_name, due_date)
        self.tasks.append(new_task)
    
    def delete_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                return True
        return False
    
    def delete_all_task(self):
        self.tasks.clear()
        self.save_to_csv()
    
    def edit_task(self, task_name, new_name=None, new_date=None):
        for task in self.tasks:
            if task.task_name == task_name:
                if new_name is not None:
                    task.change_name(new_name)
                if new_date is not None:
                    task.change_due_date(new_date)
                return True
        return False
    
    def mark_task_as_done(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                task.status_marked()
                return True
        return False
    
# if __name__ == "__main__":
#     tm = TaskManagement()
#     tm.add_task("Belajar Python", "2025-04-20")
#     tm.add_task("Makan siang", "2025-04-14")

#     print("Daftar tugas")
#     for task in tm.view_task():
#         print(f"{task.task_name} - {task.due_date} - {'v' if task.completed else 'x'}")
    
#     print("\nMenghapus 'Makan siang'")
#     tm.delete_task("Makan siang")

#     print(f"\nDelete All Task")
#     tm.delete_all_task()

#     print("Daftar tugas")
#     for task in tm.view_task():
#         print(f"{task.task_name} - {task.due_date} - {'v' if task.completed else 'x'}")
