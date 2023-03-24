#Jinny Choe
#3/22/2023
#Week 6 Homework Question #4

def main():
    writefile = open('numbers_list.txt','a') #Opens file to write
    
    writefile.write("100\n200\n300\n") #writes in file
    
    writefile.close() #closes file
    
    readfile = open('numbers_list.txt','r') #opens file for read
   
    total = 0 #initializes total
    
    for line in readfile: #loops through each line in file
        
        line = int(line.strip()) #convert to int
        
        total+= line #adds int to total
    
        readfile.close() #closes file
    
    print ("The total sum of all numbers in numbers_list.txt: ",total) #prints total sum
main()
