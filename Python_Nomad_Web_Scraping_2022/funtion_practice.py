
#RETURN 개념 

from turtle import fd


def tax_calc(money):
    return (money*0.35)
def pay_tax(tax_price):
    print ("Thank you for paying", tax_price)

tax = tax_calc(10000)
pay_tax(tax)


def calc(a,b):
    return (a+b)

result1 = calc(10,10)
result2 = calc(15,45)

print(result1)
print(result2)

def min(x,y):
    print (x-y)

min(result1,result2)

min(calc(500,350),calc(300,200))

# 변수 한번에 호출하기  (f{})

name = "tyrone"
age = "12"
eye_color = "black"
print(f"Hi my name is {name}, I have been in here for {age} years, {eye_color} is my skin color")

name = "nike"
print(f"I like {name}")


