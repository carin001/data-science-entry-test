def find_first_negatives (lst):
    i = 0
    while i < len(n):                 # run iteration less than length of items in n
        if n[i] < 0:                   #search for the first negative occurrence in n
            return (n[i])                #return the first negatives
            i = i + 1                   #increment the index if negatives not found
        else:                           #use the while loop with if and else condition
            return ("No Negatives")       #return "no negatives" if no negatives occurrences is found
        break

lst = [3, 5, -1, 7, -2, 8]
print("List:", lst)
n = [num for num in lst if num < 0]      #invoke a list comprehension to filter negative numbers
print("Output for n:", n)
result = find_first_negatives (lst)
print(result)

lst = [2, 10, 7, 0]
print("List:", lst)
n = [num for num in lst if num < 0 or num >= 0]  #invoke a list comprehension method to filter negatives or positives
print("Output for n:", n)
result = find_first_negatives (lst)
print(result)







