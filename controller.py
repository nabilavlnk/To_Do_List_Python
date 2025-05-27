from datetime import datetime

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def run(self):
        while True:
            try:
                self.view.show_menu()
                choice = int(input("Choose a menu with the number : "))

                if choice == 1:
                    # tampilkan semua tugas
                    tasks = self.model.view_task()
                    self.view.show_tasks(tasks)
                    print()

                elif choice == 2:
                    # tambah tugas
                    tasks = self.model.view_task()
                    task_name = input("Enter task name : ")
                    if any(task.task_name == task_name for task in tasks):
                        self.view.show_message(f"Task '{task_name}' already exist!")
                    else:
                        due_date = input("Enter deadline date (YYYY-MM-DD) : ")
                        try:
                            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                            due_date_formatted = due_date_obj.strftime("%d %B %Y")
                            self.model.add_task(task_name, due_date_formatted)
                            self.model.save_to_csv()
                            self.view.show_message(f"Task '{task_name}' added successfully!")
                        except ValueError:
                            self.view.show_message("Invalid date format. Use YYY-MM-DD.")
                            continue
                    print()

                elif choice == 3:
                    tasks = self.model.view_task()
                    self.view.show_tasks(tasks)
                    old_name = input("Enter task name : ")
                    found = any(task.task_name == old_name for task in tasks)
                    if not found:
                        self.view.show_message(f"Task '{old_name}' not found!")
                    else:
                        new_name = input("Enter new task name : ")
                        new_date = input("Enter new deadline date (YYYY-MM-DD) : ")

                        if new_name == "":
                              new_name = None

                        if new_date == "":
                            new_date = None

                    success = self.model.edit_task(old_name, new_name, new_date)
                    self.model.save_to_csv()
                    if success:
                        self.view.show_message(f"Task '{old_name}' edited successfully!")
                    else:
                        self.view.show_message(f"Task '{old_name}' edit canceled!")
                    print()

                elif choice == 4:
                    # hapus satu tugas
                    tasks = self.model.view_task()
                    self.view.show_tasks(tasks)
                    task_name = input("Enter task name : ")
                    if self.model.delete_task(task_name):
                        self.view.show_message(f"Task '{task_name}' deleted successfull!y")
                    else:
                        self.view.show_message(f"Task '{task_name}'  not found!")
                    self.model.save_to_csv()
                    print()

                elif choice == 5:
                    # hapus all task
                    confirm_delete = input("Are you sure to delete all task? (y/n) : ")
                    if confirm_delete == "y":
                        self.model.delete_all_task()
                        self.view.show_message("All task successfully deleted!")
                    else:
                        self.view.show_message("All task delete canceled!")
                    self.model.save_to_csv()
                    print()

                elif choice == 6:
                    # status marked as done
                    tasks = self.model.view_task()
                    self.view.show_tasks(tasks)
                    confirm_marked = input("Enter the name of completed task : ")
                    if self.model.mark_task_as_done(confirm_marked):
                        self.view.show_message(f"Task '{confirm_marked}' marked as completed!")
                    else:
                        self.view.show_message(f"Task '{confirm_marked}' not found!")
                    self.model.save_to_csv()
                    print()

                elif choice == 7:
                    print("Thank you!")
                    print()
                    break
            except ValueError:
                self.view.show_message("Invalid input! Please enter a number!")
                print()
                continue
                