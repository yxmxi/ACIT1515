# micheal is from BC
micheal = 17
legal_age = 19
if micheal >= legal_age:
    print("you can drink")

user_name = "micheal"
password = "123"
min_lenght = 10
if len(password) >= min_lenght:
    print("you registered successfully")
else:
    print("your password is too short")

#figure out if a number is even or odd
#use input() to get a number from the user
#show the user a warning if they dont have even a number
#tell user if the number is even or odd
user_number = input("Please enter a number: ")



# def odd_or_even(user_input):
#     if user_input.isnumeric():
#         if int(user_input) % 2 == 0:
#             print("your number is even")
#         else:
#             print("your number is odd")
#     else:
#     print("please enter a valid number")



#give nickname
user_input= input("Please enter another number: ")
odd_or_even(user_input)
odd_or_even("12")
# if you want to hide some code for a bit select and crt + /

def times_by_ten(n):
        print(n*10)
    if number_times_ten%2 == 0:
        print("your number is even")
    else:
        print("your number is odd")

times_by_ten(4)


def times_by_ten(n):
    return n*10

def odd_or_even(n):
    if int(user) % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")


returned_value = times_by_ten(5)
print(returned_value)

numbers = [1, 2, 3, 4, 5]

def odd_or_even(n):
    if n % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")

for number in numbers:
    odd_or_even(number)

#Im so lost