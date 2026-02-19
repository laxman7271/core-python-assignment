def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(item, "not found")

def check_item(menu, item):
    if item in menu:
        print('Availability: "' + item + ' is available"')
    else:
        print('Availability: "' + item + ' is not available"')

menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
print("Updated menu:", menu)
check_item(menu, "Pizza")
