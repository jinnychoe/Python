#Jinny Choe
#3/27/2023
#Week 7 Homework Set Question #2
        
import pickle

#Opens vegetables.dat dictionary with pickle
try:
    with open('vegetables.dat', 'rb') as file:
        vegetables = pickle.load(file)
except FileNotFoundError:
    vegetables = {} #creates new dictionary if not found

#Menu with options
while True:
    print('Vegetables and prices')
    print('1: List all vegetables')
    print('2: Add new vegetable')
    print('3: Change price of existing vegetable')
    print('4: Delete existing vegetable')
    print('5: Quit')
    num = input('Enter a number: ')

    #prints vegetables with prices
    if num == '1':
       
        if vegetables: #if there is anything in the dictionary, will give you vegetable prices
            print('Price of vegetables')
        
            for item, price in vegetables.items(): 
                print(f'{item}\t\t${price:.2f}')
        else: #if nothing in dictionary, will print msg
            print('You have not added any vegetables to the file!\n')

    #Adds vegetables and prices
    elif num == '2':
        while True:
            item = input('Enter vegetable name: ')
            while not item:
                print("Please enter a vegetable name: ")
                item = input('Enter vegetable name: ') #if there are blank spaces, will continue to ask for veg name
            if item == "": 
                break
            try: 
                price = float(input('Please input the price of the vegetable: $ ')) #asks user for price of vegetable
                vegetables[item] = price #adds price to vegetable in dictionary
                break
            except ValueError: #if a nonfloat is inputed, will throw error
                print("Invalid price.\n")
        
        print(f'{item} has been added to the list.\n')

    #Changes price of existing vegetable
    elif num == '3':
        while True:
            item = input('Enter the name of the vegetable to change: ')
            if item in vegetables:
                try: 
                    price = float(input('Enter the price of the vegetable: $'))
                    vegetables[item] = price
                    break
                except ValueError:
                    print("Invalid price.\n")
                    break
                print(f'The price of {item} has been changed to ${price:.2f}.\n')
            else:
                print(f'{item} not found on the list.\n') #if item is not found on dictionary, breaks to menu
                break
            
    #Deletes vegetable in dictionary
    elif num == '4':
        if not vegetables: 
            print ("No vegetables in vegetables.dat.\n") # if no vegetables in dictionary, breaks to menu
            continue
        item = input('Enter the name of the vegetable to delete: ')
        if item in vegetables: #if vegetable name found, deletes it
            del vegetables[item]
            print(f'{item} deleted.\n')
        else:
            print(f'{item} cannot be found on the list.\n') #if vegetable name not found, breaks to menu
        break

    #Save vegetable.dat and close program
    elif num == '5':
        file = open('vegetables.dat', 'wb') #open file
        pickle.dump(vegetables, file) #pickle saves in file
        file.close() #closes file
        print('Saving to vegetables.dat and quitting the program.\n')
        break 

    else:
        print('You must chose 1, 2, 3, 4, or 5.\n')
