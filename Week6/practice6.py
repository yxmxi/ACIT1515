from menu_data import csv_text

# call your helper functions from in here
def main():
    menu = {}
    #TODO: split the string into rows
    for line in csv_text.split("\n"):
    #TODO: loop through each line and split into pieces
        category, item = parse_item(line)
        if category in menu:
            menu[category].append(item)
        else:
            menu[category] = [item]

def parse_item(line):
    category, name, quantity. price = line.split(",")
    item ={
        "name": name,
        
    }
