from model import Task
from model import TaskManagement
from view import TaskView
from controller import TaskController

if __name__ == "__main__":
    model = TaskManagement()
    view = TaskView()
    controller = TaskController(model, view)

    controller.run()
