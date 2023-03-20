#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Project #1

#this program writes to a file
def write():
    outFile = open('myFile.txt','w') #writing to default directory
    outFile1 = open('C:\\Users\\techi\\Downloads\\File\\myFile.txt','w') #writing to a specific directory
    
    outFile.write('Jason\n')
    outFile.write('Jill\n')
    outFile.write('Jake\n')
    
    outFile1.write('Jason\n')
    outFile1.write('Jill\n')
    outFile1.write('Jake\n')
    
    outFile.close()
    outFile1.close()
    
    print ('the names have been recorded')

write()

def read():
    infile = open('myFile.txt','r')
    infile1 = open('C:\\Users\\techi\\Downloads\\File\\myFile.txt','r')
    
    fileContents = infile.read()
    fileContents1 = infile.read()
    
    infile.close()
    infile1.close()
    
    print(fileContents)
    print(fileContents1)

read()

def WriteInput(): #This function will allow user to write the input

    print("Enter the names of your friends: ")

writeMoreFriends = "Y"

while writeMoreFriends == 'Y' or writeMoreFriends == 'y':
    
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ") 
    name3 = input("Friend #3: ")
    
    FriendFile = open('friends.txt', 'a') #a is append
    
    FriendFile.write (name1 + '\n')
    FriendFile.write (name2 + '\n')
    FriendFile.write (name3 + '\n')
    
    FriendFile.close()
    print('friends recorded')
    
    writeMoreFriends = input('do you want to write more friends? type Y or y')
    
WriteInput()
    