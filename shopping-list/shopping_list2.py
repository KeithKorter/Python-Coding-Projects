import os

# Create a new empty list named shopping_list

shopping_list = []


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")
  
  
# Create a function named add_to_list that declares a parameter named item
    
def show_help():
    clear_screen()
    print("What items should we get from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'LIST' to show the list.
Enter 'REMOVE' to delete an item from your list.
""")
  
def add_to_list(item):
    show_list()
    if len(shopping_list):
      position = input("Where should I add {}?\n"
                       "Press ENTER to add to the end of the list\n"
                       "> ".format(item))
      
    else:
        position = 0
        
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        # Add item to list
        shopping_list.append(item)
    

    show_list()

    #define a function that prints show_list that prints all items in the list

def show_list():
  clear_screen()
  
  print("Here is your list:")
  
  index = 1
  for item in shopping_list:
    print("{}. {}".format(index, item))
    index += 1
    
  print("-" * 10)
  
  
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

#First function call for instructions
show_help()

#running of script commands
while True:
    new_item = input("> ")
    
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'LIST':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
    #Call add_to_list with new_item as an argument
      add_to_list(new_item)