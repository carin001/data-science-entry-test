def check_divisibility(num, divisor):
    while num < 100:          #use while loop and set num less than 100 so that num will print less than 100
        if num % divisor == 0:     #use the operator approach to check on divisibility of num
            return "True"         #apply if, else on condition num % divisor equal zero
        else:
            return "False"
            num += 1               #insert this increment num line to prevent forever loop
        break                      #add break to stop loop even if condition is true

#num = 10
#divisor = 2
result = check_divisibility(10, 2)
print(result)

#num = 7
#divisor = 3
result = check_divisibility(7, 3)
print(result)