class TaskView:
    def show_menu(self):
        print("================== MENU ==================")
        print("1. View all task")
        print("2. Add new task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Delete all task")
        print("6. Marked task as 'Done'")
        print("7. Exit")
        print("===========================================")

    def show_tasks(self, tasks):
        if not tasks:
            print("There are no task")
            return 
        
        print("-" * 58)
        print(f"| {'Task Name':<20} | {'Due Date':<20} | {'Status':<8} |")
        print("-" * 58)

        for task in(tasks):
            if task.status == True:
                status = "✓"
            else:
                status = "✗"
            #return self.tasks
            print(f"| {task.task_name:<20} | {task.due_date:<20} | {status:^8} |")

        print("-" * 58)
            #print(f"{task.task_name} (Due: {task.due_date}) [{status}]")
        
    def show_message(self, message):
        print(message)
    
# if __name__ == "__main__":
#     tv = TaskView()
#     tv.show_menu()