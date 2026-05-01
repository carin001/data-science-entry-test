def find_and_replace(lst, find_val, replace_val):
    for i, value in enumerate(lst):           #use the enumerate approach tru all occurrences of find_val
        if find_val in value:
            lst[i] = value.replace(find_val, replace_val)  #use the replace method to replace_val


    #print("find_val: ", find_val)
    #print("replace_val: ", replace_val)

    return ("modified list: ", lst)                          #return modified list


#lst = ["one", "one", "two", "three", "three", "four", "five", "six", "six", "six"] #define the list
#find_val = "six"                                                                 #define the find_val
#replace_val = "ten"                                                              #define the replace_val
result = find_and_replace((["one", "one", "two", "three", "three", "four", "five", "six", "six", "six"]), "six", "ten")
print (result)                                                                   #print the modified list



#lst = ["1", "2", "3", "4", "2", "2"] #define the list in string data type for function to work
#find_val = "2"                                                                 #define the find_val
#replace_val = "5"                                                              #define the replace_val
result = find_and_replace(["1", "2", "3", "4", "2", "2"], "2", "5")
print (result)

#lst = ["apple", "banana", "apple"]                                             #define the list
#find_val = "apple"                                                                 #define the find_val
#replace_val = "orange"                                                             #define the replace_val
result = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print (result)


