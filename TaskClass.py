import datetime
class TaskClass():
    #Temporary Storage 
    global temp_Tasks, temp_Task , x
    temp_Tasks = [['1','Task 1','Task 1 notes']] # list of lists [["1","Review Code","Review Corey's code "],["2","Stand Up ","Review Corey's code "]]
    temp_Task = [] #list containing 3 elements [<task_no>,<task_name>,<task_notes>]
    x = datetime.datetime.now().date()
    #getter method for tasks 
    def getTasks(self):
        #checking if empty 
        if(not temp_Tasks):
            print(" No tasks available for {0} ".format(x))
        else:
            #printing task if has values 
            i = 0
            for i in temp_Tasks:
                print("{0}".format(i))
                
    #setter method for tasks
    def setTasks(self):
        c = "y"
        while( c != "n"):
            #inputting : Task_No , Task_Name , Task_Num
            t_name = "" 
            t_notes = ""
            t_no = len(temp_Tasks)+1
            temp_Task.append(t_no)
            print("Input Task Name :")
            t_name = input()
            temp_Task.append(t_name)
            print("Input Task Notes : ")
            t_notes = input()
            temp_Task.append(t_notes)
            print(temp_Task)
            #appending temp_Task list into temp_Tasks list 
            temp_Tasks.append(temp_Task)
            temp_Task.clear()
            #asking if there is more task to enter
            print("Want to enter more tasks ?")
            c = input()
            if(c =="y"):
                continue
            elif(c =="n"):
                break
    #deleting method for tasks 
    def deleteTasks(self):
        print("Deleting Tasks")
    #potential update method