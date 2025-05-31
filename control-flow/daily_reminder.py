task = input("Enter your task description:")

priority = input("Priority (high/medium/low):")

time_bound =input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task and requires attention")
    case "medium":
        
        if time_bound == "yes":
            
            print(f"Reminder: '{task}' is a medium priority task that requires a immediate attention today!")  
        else:
            print(f"Note: {task} is a medium priority task and requires attention")
            
    case "low":
        if time_bound == "yes":
            
            print(f"Reminder: '{task}' is a low priority task that requires a immediate attention today!")  
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Not a valid priority")
        
     
            
            
        