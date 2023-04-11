#Jinny Choe
#4/10/23
#Week 8 Exam Question 7

biglist = [[5,6,7,8],[9,10,11,12],[13,14,15,16]] #initialize list of lists

while True:
    try: #get user input for num to find
        num = int(input("Enter the number to retrieve: ")) 
        break
    except ValueError: #throw error if not a whole number
        print("Enter a whole number.")


for lists in biglist: #goes through each sublist in biglist 
    for n in lists: #goes through each value in sublist
        if n == num:
            print(f"The number {num} is found on the list")