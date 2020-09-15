# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none

def factorial_calc(num):  
    if num == 1:
        return num
    elif num == 0:
        return 1
    else:
        return num * factorial_calc(num - 1)

if __name__ == '__main__':
    num = int(input("Enter a Number to factorialize: "))
    # Test your code with this first
    # Change the argument to try different values
   # print(factorial_calc(num))
    if num < 0:
        print("sorry we cannot find the factorial of a negative number")

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    print(factorial_calc(num))