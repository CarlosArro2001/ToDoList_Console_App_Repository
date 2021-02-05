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
    #setter method for tasks
        def setTasks(self):
            #getting amount of rows in csvfile
            with open(csv_File,'r+') as file:
                reader_file = csv.reader(file,delimiter=',')
                value = len(list(reader_file))
                print(value)
            #t_no will now contain the value of the task t_no
            t_No = str(value-1) # value - 1 because the lines add by 1
            print("Enter the task name :" )
            t_Name = input()
            print("Enter any notes :" )
            t_Notes = input()
            with open(csv_File,'a') as file:
                writer = csv.writer(file)
                writer.writerow([t_No,t_Name,t_Notes])
        #deleting method for tasks 
        #get the values in a list , delete a value from the list , write to the value 
    def deleteTasks(self):
        temp_List = []
        #reading file and putting value into an array
        with open(csv_File,encoding='utf-8-sig') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                if(not row):
                    continue
                else:
                    temp_List.append(row)
            print(temp_List)
        #asking user which value to delete
        print("Enter task number to delete task :")
        del_Num = input()
        i = 0
        found = False 
        while(i <len(temp_List)):
            if(del_Num == temp_List[i][0]):
                print("Task Found and will be deleted")
                found = True
                temp_List.remove(temp_List[i])
            i = i + 1
        if(found == True):
            print("Task has been deleted")
            print(temp_List)
            with open(csv_File ,"w") as file:
                writer = csv.writer(file)
                writer.writerows(temp_List)
                print("File Updated")
        else:
            print("Error Task not found")