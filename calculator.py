#simple calculator / simpel kalkulator

#Make variable input / membuat variabel input
operator = input("Enter Operator : ")
input1 = float(input("Enter first number : "))
input2 = float(input("Enter second number: "))

# if statement  with different operation / statement percabangan dengan operasi berbeda
if operator == "+":
    result = input1 + input2
    print(f'{input1} {operator} {input2} = {result}')
elif operator == "-":
    result = input1 - input2
    print(f'{input1} {operator} {input2} = {result}')
elif operator == "*":
    result = input1 * input2
    print(f'{input1} {operator} {input2} = {result}')
elif operator == "/":
    result = input1 / input2
    print(f'{input1} {operator} {input2} = {result}')
else :
    print('Sorry, cannot calculate')


