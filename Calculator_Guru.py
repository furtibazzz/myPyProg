import sys
import re
import math
# Start Of Speech Collection
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something...")
    audio=r.listen(source)
try:
    text=r.recognize_google(audio)
    print("You Said ->{}".format(text))
except:
    print("Oooops!! I can't hear you.SORRY! ")#end of speech collection
try:
    string1=text
    list_of_a = list(map(int, re.findall(r'(?<!\S)[+-]?\d+(?!\S)', string1)))
    numOfElement=len(list_of_a)
    if(numOfElement == 0):
        print("Yod didn't speak any numbers.")
        sys.exit(0)
except:
    print("Why are You Silent Boss?")
#FUNCTION OF MULTIPLICATION
def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
try:

    while True:
        # WORKING WITH ADDITION
        if 'sum' in string1:
            return_val = sum(list_of_a)
            print("The result is ::",return_val)
            break
        elif 'add' in string1:
            return_val = sum(list_of_a)
            print("The result is ::",return_val)
            break
        elif "addition" in string1:
            return_val = sum(list_of_a)
            print("The result is ::",return_val)
            break
        # WORKING WITH SUBSTRACTION
        elif "substract" in string1:
            sub_val = list_of_a[0] - list_of_a[1]
            print("The result is ::",sub_val)
            break
        elif "sub" in string1:
            sub_val = list_of_a[0] - list_of_a[1]
            print("The result is ::",sub_val)
            break

        elif "substraction" in string1:
            sub_val = list_of_a[0] - list_of_a[1]
            print("The result is ::",sub_val)
            break
        elif 'multiply' in string1:
            print("The result is ::",multiplyList(list_of_a))
            break
        elif 'multiplication' in string1:
            print("The result is ::",multiplyList(list_of_a))
            break
        elif 'divide' in string1:
            return_val = list_of_a[0] / list_of_a[1]
            print("The result is ::",return_val)
            break
        elif 'division' in string1:
            return_val = list_of_a[0] / list_of_a[1]
            print("The result is ::",return_val)
            break
        elif 'gcd' in string1:

            gcd_val = math.gcd(list_of_a[0], list_of_a[1])
            print("The result is ::",gcd_val)
            break
        elif "binary of" in string1:
            a = list_of_a[0]
            ele=bin(a)
            print(ele[2:])
            break
        elif "binary" in string1:
            a = list_of_a[0]
            ele=bin(a)
            print(ele[2:])
            break
        elif "binary form" in string1:
            a = list_of_a[0]
            ele=bin(a)
            print(ele[2:])
            break
        #Hexadecimal of a number
        elif "hexadecimal of" in string1:
            a=list_of_a[0]
            ele=hex(a)
            print(ele[2:])
            break
        elif "hexadecimal" in string1:
            a=list_of_a[0]
            ele=hex(a)
            print(ele[2:])
            break
        elif "hexadecimal form" in string1:
            a=list_of_a[0]
            ele=hex(a)
            print(ele[2:])
            break
        #octal of a number
        elif "octal of" in string1:
            a=list_of_a[0]
            ele=oct(a)
            print(ele[2:])
            break
        elif "octal" in string1:
            a = list_of_a[0]
            ele=oct(a)
            print(ele[2:])
            break
        elif "octal form" in string1:
            a = list_of_a[0]
            ele=oct(a)
            print(ele[2:])
            break
        elif "decimal" in string1:
            stringToDec = list(map(str, re.findall(r'(?<!\S)[+-]?\d+(?!\S)', string1)))
            a = stringToDec[0]
            print(int(a,2))
            break
        elif "square root" in string1:
            x=list_of_a[0]
            sqrt_val=math.sqrt(x)
            print("The result is:",sqrt_val)
            break
        elif "square" in string1:
            x=list_of_a[0]
            print("The result is:",x**2)
            break
        elif "to the power" in string1:
            if(numOfElement>2):
                print("I can calculate for Two integer value only,Sorry..!")
                break
            else:
                x=list_of_a[0]
                y=list_of_a[1]
                print("The result is:",x**y)
                break
        else:
            print("Nothing to do,I am Very Happy :>)")
            break
except:
    print("Run again and try")