task_list = ['ghj','jkl','uyt']
def main_menu():
        print('''options to select (1-6)
            1) add Task
            2) remove Task
            3) update Task
            4) view Task
            5) complete Task
            6) exit''')
        choice=(input('enter number from 1-6: '))
        if choice=="1":
            add_task()
        if choice=="2":
            remove_task()
        if choice=="3":
            update_task()
        if choice=="4":
            view_task()
        if choice=="5":
            complete_task()
        if choice=="6":
            out()
        else:
            print('please enter valid option:')
            main_menu()


def add_task():
    
    task = input("enter task: ")
    task_list.append(task)
    print(task_list)
    conti()

 
def remove_task():
    for i in task_list:
        print(i)
    try:  
        task = input("enter task to remove: ")
        
        task_list.remove(task)
        
            
        for i in task_list:
            print(i)
        conti()
    except:    
            print("task is not present in list:")
            remove_task()

def update_task():
    for i in task_list:
        print(i)
    task = input("enter task to update: ")
    new_task=input('new task: ')
    x=task_list.index(task)
    task_list[x]=new_task
    for i in task_list:
        print(i)
    conti()

def view_task():
    print("list of pending task")
    for i in task_list:
        print(i)
    conti()

def complete_task():
    for i in task_list:
        print(i)
    task=input('enter done task: ')
    new_task=f"\033[9m {task} \033[0m"
    x=task_list.index(task)
    task_list[x]=new_task
    for i in task_list:
        print(i)
    conti()

def out():
    print("now you are out of the app ")
def conti():
    con=input('want to continue or exit (Y/N): ')
    if con=='y'or'Y':
        main_menu()
    if con=='n'or'N':
        out()
main_menu()
