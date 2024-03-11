to_do_list = []
def add_task(task):
    to_do_list.append(task)
    print("Newly added task :" + task)

def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task has been removed :" + task)
    else:
        print("Task is not present...")

def show_task():
        if not to_do_list:
            print("list is empty")
        else:
            print("To do list ")
            for index,task in enumerate(to_do_list):
                print(f" {index + 1}.{task} ")

while True:
    print("\n options:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show  To do Task")
    print("4. Quit")


    choice = input("enter  u r choice (1/2/3/4)")

    if choice == '1':
        task = input("Enter task ")
        add_task(task)
    elif choice == '2':
        task = input("enter task no to remove ")
        remove_task(task)
    elif choice == '3':
        show_task()
    elif choice == '4':
        print("thank you")
        break
    else :
        print("invalid ...try again")
