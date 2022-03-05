#github task
#task 1

""" 
NAME : ABHAY VG
TASK : STRING REVERSE
DATE OF CREATION : 4/02/2022
DATE OF UPDATION : 4/02/2022

"""
def Reverse_String(String):
    return String[::-1]

Strin= "IamLearningInSOU"
new_String = Reverse_String(Strin)
print(new_String)

#task 2

""" Name: Divyesh Patel
    Task: Add in list +2
    Date(Created): 4 March 2022
"""
# function of adding 2 in list
def addinilist(lst):
   new_lst = [new+2 for new in lst] #one liner for loop for adding modified list
   print(new_lst) #printed modified list

ls = [1, 2, 3, 4] #list
addinilist(ls) #function executed
#github task
#task 3

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
