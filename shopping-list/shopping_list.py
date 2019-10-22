# Create a new empty list named shopping_list

shopping_list = []


# Create a function named add_to_list that declares a parameter named item
    
def show_help():
    print("What items should we get from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'LIST' to show the list.
""")
  
def add_to_list(item):
    # Add item to list
    shopping_list.append(item)
    
    # Notify user item was added and item count
    print("{item} Added! List has {num} items.".format(item=item, num=len(shopping_list)))
    

    #define a function that prints show_list that prints all items in the list

def show_list():
  print("Here is your list:")
  for item in shopping_list:
    print(item)

#First function call for instructions
show_help()

#running of script commands
while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'LIST':
        show_list()
        continue
      
    #Call add_to_list with new_item as an argument
    add_to_list(new_item)