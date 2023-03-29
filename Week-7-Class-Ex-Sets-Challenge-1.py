#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Challenge #1

#This program demonstrates various set operations.
baseball = set(['Jodi','Carmen','Aida','Alicia',])
basketball = set(['Eva','Carmen','Alicia','Sarah'])

#Display members of the baseball set
print('The following students are on the baseball team')
for name in basketball:
    print(name)

#Demonstrate intersection
print()
print('The following students play both baseball and basketball: ')
for name in baseball.intersection(basketball):
    print(name)

#Demonstrate union
print()
print('The following students play either baseball or basketball: ')

for name in baseball.union(basketball):
    print(name)

#demonstrate difference of baseball and basketball
print()
print('The following students play baseball, but not basketball: ')
for name in baseball.difference(basketball):
    print(name)

#demonstrate difference of basketball and baseball
print()
print('The following students play basketball, but not baseball: ')
for name in basketball.difference(baseball):
    print(name)

#demonstrate symmetric difference
print()
print('The following students play one sport, but not both: ')
for name in baseball.symmetric_difference(basketball):
    print(name)
