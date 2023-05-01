#Q1

# fname = input("enter your First Name : ")
# lname = input("enter your Last Name : ")
# txt1 = fname [::-1]
# txt2 = lname [::-1]
# print (txt2 + " " + txt1)
#_________________________________________________________________________________
#Q2

# n = int(input("enter the number : "))
# n1 = int( "%s" % n )
# n2 = int( "%s%s" % (n,n) )
# n3 = int( "%s%s%s" % (n,n,n) )
# print ('Expected Result : ', n1+n2+n3)
# _______________________________________________________________________________
# Q3

# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)
#__________________________________________________________________________________
# Q4

# import math
# r = int(input("enter raduis : "))
# V= 4.0/3.0*math.pi* r**3
# print('The volume of the sphere is: ',V)
#________________________________________________________________________________________
#Q5

# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("area = ", area)
#___________________________________________________________________________________
# Q6

# n=5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')
    
# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
#_____________________________________________________________________________________
# Q7

# w = input("enter word : ")
# txt1 = w [::-1]
# print (txt1)
#_________________________________________________________________________________
# Q8

# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x)
#___________________________________________________________________________________
#Q9

# x,y=0,1
# while y<50:
#     print(y)
#     x,y = y,x+y
#____________________________________________________________________________________
#Q10
# s = input("enter a string : ")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)
	
	




