'''
valid = input("")
while  ():
'''

guest_number = input("How many guests do you have?")
guest_number = int(guest_number)
if guest_number > 8:
    print("Sorry, we don' t have enought spare seats.")
else:
    print("Yes, come in.")

ingredients = []
while True:
    ingredient = input("Please: ")
    if ingredient != 'quit':
        ingredients.append(ingredient)
    else:
        break

