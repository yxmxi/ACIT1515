from menu_data import csv_text

# call your helper functions from in here

def print_formatted():
    return 0

def main():
    all = csv_text.replace("\n", ",").split(",")

    Menu = {}

    MealType = "temp"
    MealName = "temp"
    i = 1

    for word in all:
        i = all.index(word) + 1

        if i % 4 == 1: # get meal type 
            if word not in Menu:
                Menu[word] = {}
            MealType = word

        elif i % 4 == 2: # get meal name
            if word not in Menu[MealType]:
                Menu[MealType][word] = {}
            MealName = word

        elif i % 4 == 3: # set quantity
            Menu[MealType][MealName]["Quantity"] = word
        else: #set price
            Menu[MealType][MealName]["Price"] = word

        i += 1 #increment by 1

    #print in format
    for Meal in Menu:
        print(f"* {Meal} Items *")

        for Name in Menu[Meal]:
            M =  Menu[Meal][Name]
            print(f"{M["Price"]} {Name}, {M["Quantity"]}")
        
        print("")

    # print(Menu)
            

main()