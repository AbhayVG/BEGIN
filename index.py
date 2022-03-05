'''
NAME:ARYAN ACHARYA
CREATED ON:4/03/2022
TASK:SWAPPING A=10,B-20 TO A=20,B=10

'''
#UDF to swap two varaibles
def swaptwo(x,y):
    x,y = y,x #swap logig
    print("Values after swapping:\n{x},{y}") #this will print swaped values

a=10 #var-1
b=20 #var-2
print("Values before swapping:\n{x},{y}") #this will print original values
swaptwo(a,b) #swap function used.