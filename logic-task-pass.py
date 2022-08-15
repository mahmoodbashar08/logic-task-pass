# Q1
def removeCharacter(myString, myCharacter):
    # to replace the character with new from a string
    return myString.replace(myCharacter, "")


myString = input("enter the string : ")
myCharacter = input("enter the character that you want to remove : ")
newString = removeCharacter(myString, myCharacter)
print(newString)


# Q2
while True:  # to check that the first number is always integers
    try:
        firstNumber = int(input("enter the first number : "))
        break
    except:
        print("That's not a valid option!")

while True:  # to check that the second number is always integers independently
    try:
        secondNumber = int(input("enter the second number : "))
        break
    except:
        print("That's not a valid option!")

primeNumbers = []
for n in range(firstNumber, secondNumber+1):  # (+1) to take the last number in range
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            primeNumbers.append(n)
print("all prime number : ")
print(primeNumbers)


# Q3
def repeated(myString, myCount, myCharacter):
    # to convert the string to a list and save it to new variable
    newstring = list(myString)
    for i in range(len(newstring)):
        # to comparison given character with each character in the list
        if myCharacter == newstring[i]:
            myCount = myCount + 1
    return myCount


myString = input("enter the string : ")
myCharacter = input("enter the character you want to count : ")
myCount = 0
newCount = repeated(myString, myCount, myCharacter)
print("repeated " + str(newCount) + " times")
