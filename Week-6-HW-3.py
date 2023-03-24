#Jinny Choe
#3/22/2023
#Week 6 Homework Question #3

def main():
  
    file = open('number_list.txt','a') #opens file for append
   
    i = 1 #initializes variable
        n=1
    
    for i in range(100): #runs loop to write out numbers 1 - 100
      
        i += 1 #add to iteration

        file.write(str(n)+'\n') #writes to file
        
        n += 1 #adds to number
        
    file.close() #closes file
    
main()
