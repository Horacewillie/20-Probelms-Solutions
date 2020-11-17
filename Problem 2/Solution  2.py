import random

def rand():
    global string
    string  = " "
    for i in range(3):
        num = random.randint(0,9)
        string = string + " " + str(num)
    string = string.lstrip()
    print(string)

while True:
    input("Press any key: ").lower()

    rand()

    if "7" not in string:
        print("Try again! Better luck next time.!")
        
    else:
        print("Congratulations!")
        print("You are a lucky chap")
        break



    
    



