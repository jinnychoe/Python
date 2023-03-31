#Jinny Choe
#3/27/2023
#Week 7 Homework Set Question #2
        
import pickle

#Opens vegetables.dat dictionary with pickle
try:
    with open('vegetables.dat', 'rb') as file:
        vegetables = pickle.load(file)
except FileNotFoundError:
    vegetables = {}

#Menu with options
while True:
    print('Vegetables and prices')
    print('1: List all vegetables')
    print('2: Add new vegetable')
    print('3: Change price of existing vegetable')
    print('4: Delete existing vegetable')
    print('5: Quit')
    num = input('Enter a number: ')

    #Lists vegetables with prices
    if num == '1':
        
        if vegetables:
            print('Price of vegetables')
        
            for veg, price in vegetables.items():
                print(f'{veg}\t\t${price:.2f}')
        else:
            print('You have not added vegetables to the file\n')

    #Adds vegetables and prices
    elif num == '2':
        while True:
            veg = input('Enter vegetable name: ')
            while not veg:
                print("Please enter a vegetable name: ")
                veg = input('Enter vegetable name: ')
            if veg == "":
                break
            try: 
                price = float(input('Please input the price of the vegetable: '))
                vegetables[veg] = price
                break
            except ValueError:
                print("Invalid price.\n")
        
        print(f'{veg} has been added to the list.\n')

    #Changes price of existing vegetable
    elif num == '3':
        while True:
            veg = input('Enter the name of the vegetable to change: ')
            if veg in vegetables:
                try: 
                    price = float(input('Enter the price of the vegetable: '))
                    vegetables[veg] = price
                    break
                except ValueError:
                    print("Invalid price.\n")
                    break
                print(f'The price of {veg} has been changed to ${price:.2f}.\n')
            else:
                print(f'{veg} not found on the list.\n')

    #Deletes vegetable on list
    elif num == '4':
        if not vegetables:
            print ("No vegetables in vegetables.dat.\n")
            continue
        veg = input('Enter the name of the vegetable to delete: ')
        if veg in vegetables:
            del vegetables[veg]
            print(f'{veg} deleted.\n')
        else:
            print(f'{veg} cannot be found on the list.\n')
        break

    #Save vegetable.dat and close program
    elif num == '5':
        with open('vegetables.dat', 'wb') as file:
            pickle.dump(vegetables, file)
        print('Saving to vegetables.dat and quitting the program.\n')
        break

    else:
        print('You must chose 1, 2, 3, 4, or 5.\n')
