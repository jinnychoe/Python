#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Project #5

def main():
    food = ['Pizza','Burgers','Chips']
    print('here are the food items in the list')
    print(food)
    item = input('which items in the list do you want to change?')
    
    try: #the try statement will try the batch of code below
        itemIndex = food.index(item) #gets the items index in the list
        newItem = input('Enter the new value: ') #ter the value to replace with
        food[itemIndex]  = newItem #replace the old item with the new item
        print('Here is the revised list ')
        print(food)
    except ValueError:#if an error is found it will print the error
        print('the item was not found in the list')

main()