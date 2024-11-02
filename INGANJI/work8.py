from datetime import datetime

def greet_user():

    current_time = datetime.now().time()


    morning_start = current_time.replace(hour=5, minute=0, second=0, microsecond=0)
    afternoon_start = current_time.replace(hour=12, minute=0, second=0, microsecond=0)
    evening_start = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
    night_start = current_time.replace(hour=21, minute=0, second=0, microsecond=0)

    
    if morning_start <= current_time < afternoon_start:
        print("Good morning!")
    elif afternoon_start <= current_time < evening_start:
        print("Good afternoon!")
    elif evening_start <= current_time < night_start:
        print("Good evening!")
    else:
        print("Good night!")
greet_user()

  
print("1.Inganji fiscal clovis,2.Isingizwe luckyson,3.Kirabo lucille,4,Gasore boris")
