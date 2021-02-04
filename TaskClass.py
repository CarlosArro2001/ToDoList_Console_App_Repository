import datetime
import csv
class TaskClass():
    #Temporary Storage 
    global temp_Tasks, temp_Task , x , csv_File 
    temp_Tasks = [] # list of lists [["1","Review Code","Review Corey's code "],["2","Stand Up ","Review Corey's code "]]
    Task = [] #list containing 3 elements [<task_no>,<task_name>,<task_notes>]
    csv_File = "TaskList.csv"
    x = datetime.datetime.now().date()
    #getter method for tasks 
    def getTasks(self):
        with open(csv_File,'r') as file:
            reader=csv.reader(file,delimiter=',')
            for row in reader: 
                if(not row):
                    continue
                else:
                    temp_Tasks.append(row)
            if(temp_Tasks[0][0]=='ï»¿No '):
                temp_Tasks.remove(temp_Tasks[0])
            i = 0
            while(i <len(temp_Tasks)):
                print("\n {0}. {1} \n notes: \n{2}".format(temp_Tasks[i][0],temp_Tasks[i][1],temp_Tasks[i][2]))
                i = i+1
            
                    
        '''
        if(not temp_Tasks):
            print(" No tasks available for {0} ".format(x))
        else:
            #printing task if has values 
            i = 0 
            print("\n \n Task List :")
            while(i < len(temp_Tasks)):
                print(temp_Tasks[i][0])
                print("Task Name : {0}".format(temp_Tasks[i][1]))
                print("Notes :\n {0}".format(temp_Tasks[i][2]))
                i = i+1
            print("\n")
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