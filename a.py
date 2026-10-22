def add (x,y):
    return x+y
def subtract(x,y):
        return x-y 
def multiply(x,y):
            return x*y
def divide (x,y):

            return x/y
print("give the number")
print(" 1.add ")
print(" 2.sub")
print ("3 multiply")
print ("4 divide")
select = input(" enter the choice ")
num1=int(input("enter 1 no. "))
num2=int(input("enter 2 no"))
if select == '1':
      print (num1,"+",num2 ,"=" ,add(num1,num2 ))
elif select == '2':
      print( num1, "-" , num2,"=", subtract(num1,num2))
elif select == '3' :
       print (num1 ,"*",num2,"=", multiply(num1 , num2 ))
elif select == '4':
     print(num1 ,"/",num2 ,"=" ,divide ( num1,num2))


                            




