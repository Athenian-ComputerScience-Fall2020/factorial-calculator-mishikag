# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none

def factorial_calc(num):  
    if num == 1:
        return num
    else:
        return num * factorial_calc(num - 1)

num = int(input("Enter a Number to factorialize: "))

while num < 0:
    num = int(input("sorry we cannot find the factorial of a negative number"))
if num == 0:
    print("the factorial for 0 is 1")
else:
    print("working")


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(factorial_calc(num))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))