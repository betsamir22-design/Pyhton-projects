my_tasks=["wash my hands","vuying groceries"]

while True:
  question1=input("add or delete or exit or show? :").strip().lower()

  


  if question1 in["add","a"]:
    
    user_task=input("Write your tasks: ").strip()
    if user_task in my_tasks:
        print("task exists")
    else:
        

     my_tasks.append(user_task)
     print("tasks")
     for task in my_tasks:
        print(task)
  elif question1 in ["delete","d"]:
    user_task=input("Write your tasks1 that you want to delete:  ").strip()
    if user_task in my_tasks:
        
     my_tasks.remove(user_task)
     print("tasks")
     for task in my_tasks:
         print(task)
    else:
        print("the task was not found")
  elif question1 in["exit","e"]:
      break
  elif question1 in["show","s"]:
      if len(my_tasks)>0:
          
       print("tasks")
       for task in my_tasks:
          print(task)
      else:
          print("no tasks found")
  else:
      
    print("sorry,choose delete,add,or exit")
  
    

    
