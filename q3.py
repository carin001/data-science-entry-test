def update_dictionary(dct, key, value):
    if key in dct:                                 #use the check if keys exists approach
        print ("original dictionary: ", dct)        #print original dictionary items
        x = dct.values()                           #set x to dictionary values
        print ("original value:", x)                #print original value
        dct[key] = value                           #update value
        print ("updated value:", x)                 #return the updated value
        return ("updated dictionary: ", dct)         #return the updated dictionary
    else:
        print("original dictionary: ", dct)        #print original dictionary
        x = dct.keys()                             #set x to dictionary key
        dct[key] = value                           #update key and value
        return ("updated dictionary: ", dct)         #return updated dictionary


#dct = {"age": 25}
#key = "age"
#value = 26
result = update_dictionary({"age": 25}, "age", 26)
print (result)


#dct = {}
#key = "name"
#value = "Alice"
result = update_dictionary({}, "name", "Alice")
print (result)

