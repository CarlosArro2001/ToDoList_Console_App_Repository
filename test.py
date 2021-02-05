import csv
global csv , temp_List
task_File = "TaskList.csv"


def deleteTasks():
    temp_List = []
    #reading file and putting value into an array
    with open(task_File,encoding='utf-8-sig') as file:
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
        with open(task_File ,"w") as file:
            writer = csv.writer(file)
            writer.writerows(temp_List)
            print("File Updated")
    else:
        print("Error Task not found")

deleteTasks()