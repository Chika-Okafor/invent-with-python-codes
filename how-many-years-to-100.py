def data_collector():
    print("Please, enter your name.")
    user_name = input()

    print("Hello, " + user_name + ". Please, enter your age.")
    user_age = int(input())

    years_to_100 = 100 - user_age
    year_100th = 2020 + years_to_100
    print(user_name + ", you will be 100 years old in " + str(year_100th))
    
new_user = "yes"
while new_user == "yes":
    data_collector()
    print("Do you want to check for someone else (yes or no)?")
    new_user = input()
    
