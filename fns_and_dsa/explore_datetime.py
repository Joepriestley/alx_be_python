from datetime import datetime ,timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")   
    print(f"Current date and time: {formatted}")
    
display_current_datetime()

days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    future_date = datetime.now().date() + timedelta(days)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    
    
calculate_future_date(days) 