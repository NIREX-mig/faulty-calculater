#faluty calculater
 #45*3=555, 56+9=77, 56/6=4 faulty calculation

print("This faulty calculater make by Ashish(Nirex)")

print("chose oprater")
print("+ for add ")
print("- for subtract")
print("* for multiply ")
print("/ for divide ")

while(True):
    oprater=input("chose oprater:\n")

    print("Enter first number :")
    num1=int(input())
    print("Enter secound number :")
    num2=int(input())

    if num1 is 45 and num2 is 3 and oprater is'*' : #faulty situation
        print("Ans : ", 555)
    elif num1 is 56 and num2 is 9 and oprater is '+':
        print("Ans : " ,77)
    elif num1 is 56 and num2 is 6 and oprater is '/':
        print("Ans : ", 4)

    elif oprater=='+': #correct situation
        print("Ans : ", num1 + num2)
    elif oprater == '-':
        print("Ans : ", num1 - num2)
    elif oprater == '*':
        print("Ans : ", num1 * num2)
    elif oprater == '/':
        print("Ans : ", num1 / num2,"\n")

    else:
        print("unexpected")
     
