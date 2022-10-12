#쥬수 먼둘가
def make_juice(fruit):
    return f"{fruit} + 🥤"

def add_ice (juice):
    return f"{juice} + 🧊"

def add_sugar(iced_juice):
    return f"{iced_juice} + 🧂"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print (perfect_juice)


#숫자를 더하고 제곱을 구하기
def add (a,b):
    print (f"{a}와{b}을(를) 더하면 {a+b}이고 ")
    return a+b
def sqare (add_result):
    print (f"더한 값의 {add_result} 의 제곱은 {add_result**2}이다")

add_result=add(5,3)
sqare(add_result)


def number(a):
    print(f"초기 값은 {a}입니다.")
    return a

def add_number(b):
    print (f"초기 값의 두배는 {b * 2} 입니다.")
    return b * 2

def sqare_number(c):
    print (f"두번째 값의 제곱은 {c ** 2}입니다.")
    return c ** 2

first = number(2321324)
second = add_number(first)
third = sqare_number(second)


def matome(a):
    return a , a*2, (a*2)**2

result = matome(2321324)
print(result)