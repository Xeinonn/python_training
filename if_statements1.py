#Training with comparison. Let's use 5 numbers, The highest number should be returned. If the number is 777, you got the lucky number.
#Has to be improved, if you type 777, it returns also the variable t1, but it is not needed in that case.
def casino(num1, num2, num3, num4, num5):
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        return num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        return num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        return num3
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num2 >= num5:
        return num4
    elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
        return num5
    elif num1 == 777 or num2 == 777 or num3 == 777 or num4 == 777 or num5 == 777:
        return print("You cracked the lucky number 777 and won the Jackpot!") 
    else: 
        print("Please call the function with 5 different numbers to let it work properly.")
t1 = "is the highest number."
print(casino(1000, 465, 897, 777, 256), t1)