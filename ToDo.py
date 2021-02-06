import sys 
from TaskClass import TaskClass

class ToDo(TaskClass):
    global tc 
    tc = TaskClass()
    def menu():
        c = 0
        while( c != 3):
            #getting tasks 
            print("\t \t \t WELCOME CARLOS , we are retrieving your tasks: ")
            tc.getTasks()
            print("Press 1 : Set New Tasks ")
            print("Press 2 : Delete Tasks")
            print("Press 3 : Exit Program")
            print("Input here : ")
            c = int(input())
            if(c==1):
                tc.setTasks()
            elif(c==2):
                tc.deleteTasks()
            elif(c==3):
                print("\t \t EXITING TO DO LIST ")
                sys.exit()
    menu()