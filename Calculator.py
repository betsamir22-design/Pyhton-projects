print("#"*50)
view="calculator"
print(view.center(46,"="))
print("#"*50)


while True:
   number1=int(input("write your first number :"))
   operation=input("choose an operation (+,*,/,-):")
   number2=int(input("write your second number:"))

   if operation=="+":
       print(number1+number2)
   elif operation=="-":
      print(number1-number2)
   elif operation=="/":
    if number2==0:
        print("math error, division by zero is not valid")
    else:
        print(number1/number2)
   elif operation=="*":
      print(number1*number2)
   else:
      print("this is an invalid operation,choose(+,*,-,/):")
    