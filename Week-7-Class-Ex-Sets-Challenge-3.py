#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Challenge #3

#this program will add to the list and delete from the list
def main():
    names = ['Howard','Jamie','Jill']
    #element  0          1       2
    
    print(' the list before the insert or remove ')
    print(names)
    
    NameRemove = input(' enter the name to remove ')
    
    names.insert(0,'Joe') #insert the new name at element 0, or moving or shifting element 0 to 1
    names.remove(NameRemove)#removes the name from the list
    print('the list after the insert ')
    
    print(names)

main()

def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum+=value #total the numbers in the list
    average = sum/len(numbers)
    print('The total is ',sum,'. The average is ',average)

    file = open('outputnum.txt','a')
    numbers_string = ' '.join([str(num) for num in numbers]) #convert list of numbers to string of numbers
    file.write(numbers_string+'\n')
    file.write('The total is '+str(sum)+'. The average is '+str(average))
    file.close()
total()
        
