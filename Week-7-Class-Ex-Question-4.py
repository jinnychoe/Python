#Jinny Choe
#3/27/2023
#Week 7 Class Exercise 4

#this program reads test scores from a csv file and calcualtes each student's test average

def main():
        #open file
        csv_file = open('test_scores.csv','r')
        
        #read the file's lines into a list
        lines = csv_file.readlines()
        
        #close the file
        csv_file.close()
        
        #process the lines
        for line in lines:
            #get the test scores as tokens
            tokens = line.split(',')
           
            #calcualte the total fo the test scores
            total = 0.0
            for token in tokens:
                total += float(token)
            
            #calculate the average of the test scores
            average = total/len(tokens)
            print(f'Average: {average}')

#execute the main function
if __name__ == '__main__':
    main()


