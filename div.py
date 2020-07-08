def divide(num1, num2):
    count = 0
    if num1 != num2:
        while num1 >= num2:
            num1 = num1 - num2
            count += 1
        print("Division: " + str(count))
    else:
        if count == 0:
            print("Division: 1")
        else:
            print("Division: " + str(count))


dividend = int(input("Enter dividend: "))
divisor = int(input('Enter divisor: '))
divide(dividend, divisor)
