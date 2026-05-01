#x = 20                             #just normal try to define variables
#y = 30
#print("y:", y)
#print(type(x))                   #just finding out the data types so as for further tasks later
#print(type(y))

def swap(x, y):                 #define a function name swap()
    if type(x) == str and type(y) == str: #use the if method on data type to ensure str and not int
        return -1
    else:
        x, y = y, x             #use the tuples unpacking approach to swap values
        return ("x:", x, "y:", y)

#x = 20
#y = 30
#x, y = 20, 30
#print(type(x))
#print(type(y))
#result = swap(20, 30)
#print (result)

#x = "apple"
#y = 10
#print(type(x))
#print(type(y))
#x, y = "apple", 10
result = swap("apple", 10)                          #assign result equal to swap(x,y)
print (result)                                            #print result

#x = 9
#y = 17
# x, y = 9, 17
#print(type(x))
#print(type(y))
result = swap(9, 17)
print (result)                                           #print result





