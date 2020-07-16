#receive input for what character to use for the diamond
#assign character to string character
character = input("What character should I make a diamond out of?")

#variables use the string
#Make variable 1
l1 = "    " + character + "    "
#Make variable 2
l2 = "   " + character + " " + character + "   "
#Make variable 3
l3 = "  " + character + "   " + character + "  "
#Make variable 4
l4 = " " + character + "    " + character + " "
#make variable 5
l5 = character + "     "+ character

#print the variables in this order:
#1,2,3,4,3,2,1
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l4)
print(l3)
print(l2)
print(l1)