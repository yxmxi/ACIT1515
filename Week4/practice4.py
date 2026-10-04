# fruits = ["apple", "banana", "pear"]


# for i, fruit in enumerate(fruits):
#     print(fruit, i)

#i = 0
# while i < 3
    # print(fruits[i])
    # i = i + 1

# for i in range(10):
#     print(fruit)
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# year = 2026
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for month in range(12):
#     for day in range(1, days_in_month[month] + 1):
#         print(f"{month + 1}-{day}-{year}")
# colors = [{"red": "f5291b"}, {"orange": "f57c00"}, {"yellow": "fdd835"}, {"green": "43a047"}, {"blue": "1e88e5"}, {"purple": "8e24aa"}]
#  colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]
#  print(colors_list[1])

#  #{"0": "red", "1": "orange", "2": "yellow", "3": "green", "4": "blue", "5": "purple"}

# colorss = {"red": "f5291b", "orange": "f57c00", "yellow": "fdd835", "green": "43a047", "blue": "1e88e5", "purple": "8e24aa"}
# colors["red"] 

# for key, value in colors():
#     print(key, colors)

# functions = f(x)
# name = " Hugh Jackman " 
# # name.strip() #removes whitespace from the beginning and end of a string
# # 'hugh jackman'
# # " hugh jaCkman ".lower() #converts all characters in a string to lowercase
# name.strip().lower() #removes whitespace from the beginning and end of a string and converts all characters in a string to lowercase

# name = " Hugh JaCkman "
# def clean_name(name):
#     print(name.strip().lower())
#     clean_name(name)]
# def create_username(name):
#     print("@" + name.replace(" ", "_"))

# def clean_name(name):
#         return name.strip().lower()
#         #python knows becausem of the name of the fuction and where its opened
# cleaned_name = clean_name("hugh jackman      ")
# print(cleaned_name)
# # "@" + "hughjackman".replace(" ", "_")

# def create_url(username):
#     return"http://x.com/" + username[1:]


# username = create_username(cleaned_name)
# "@hugh_jackman"[0]
# "hugh_jackman"[1]
# "@hugh_jackman"[1:] #slicing

# print(create_url(create_username(clean_name("hugh jackman      "))))

quiz notes 
list of values
values = ["red", "blue", False, 30.5]
get_length = len(values)
type()
