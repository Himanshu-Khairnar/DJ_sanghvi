employeeList = ["Joe", "Nikhil", "Veeraj"]
name = input("Enter your name: ")

def Middleware(func):
    def inner(*args, **kwargs):
        if name not in employeeList:
            print("You can't access the program as you are not authenticate user.")
            return
        return func(*args, **kwargs)
    return inner

@Middleware
def checkAuth():
    print("Your are authenticated!!!")
    print("HOMEPAGE of AMAZON: ")
    print("1. Check Shopping Chart: ")
    print("2. Check Electronics: ")
    print("3. Check Cloth: ")
    print("4. Check Orders: ")
    print("5. Exit the code")

    while(True):
        types = input("\n Enter your choices: ")
        match(types):
            case '1':
                print("\n Iphone 15 || price: 60,000/- || quantity: 1")
                print(" Total price: 60,000/-")
            case '2':
                print("\n Iphone 15 || price: 60,000/- ||")
                print(" samsung s24 ultra || price: 60,000/- ||")
            case '3':
                print("\n Short pants || price: 600/- ||")
                print(" shirt || price: 1000/- ||")
            case '4':
                print("\n Shirt || price: 1050/- || Delivery expected till FRIDAY 10/4/2025 ")
            case '5':
                print(" Bye bye!!!")
                break

checkAuth()
