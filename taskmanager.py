tasks=['dfg','asd','iop']
def main_menu():
    print("""1- add task
          2- remove task
          3- upgrade task
          4- view task
          5- complete task
          6- exit
          """)
    c = input ("what you want to do:")
    if c =='1':
        global x
        x = input()
        add_task(x)
    # if c == '2':
    #     remove_task()

def conti():
    b = input('do you want to continue or exit (y or n):')
    if b=='y' or b=='Y':
        main_menu()
    elif b=='n' or b=='N':
        print('out of program')

def add_task(x):
    tasks.append(x)
    if len(tasks)>0:
        
        for i in range(1,len(tasks)+1):
            print(i,end='')
            print(tasks[i-1])         
    
    # x = input('task to remove:')
    # tasks.remove(x)
    print(tasks)
    conti()

main_menu()

