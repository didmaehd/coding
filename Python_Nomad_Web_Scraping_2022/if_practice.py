

from random import randint
import string

# age = int(input("How old are you? "))
# print (f"You are {age} years old")

# if age < 18:
#     print ("You can't drink")
# elif age >= 18 and age < 35:
#     print ("You can drink much")
# else :
#     print ("Go ahead")


#숫자 맞추기  
# random 함수 사용
#input 함수 사용
# user_choice = int(input("Choose number. "))
# pc_choice = randint(1,50)
# print ("Welcome!")
# print (f"You chose {user_choice} and PC chose {pc_choice}")

# if user_choice == pc_choice:
#     print ("You won!")
# elif user_choice > 50 or user_choice < 0 :
#     print ("You muse insert number between 0 and 50")
# elif user_choice > pc_choice:
#     print ("You nember is too high")
# elif user_choice < pc_choice:
#     print ("You nember is too low!")


#while 연습
name = input("What's your name : ")
pc_choice = randint(1,50)
print (f"Welcome {name} !. Can you guess the number that PC chose?")
playing = True
while playing:
    user_choice = int(input("Choose number. : "))
    if user_choice == pc_choice:
        print ("You won!") # 정답이면 게임 종료 - while가 더이상 실행되지 않게 playing 값을 false 로 변경
        print ("Game Over!")
        playing = False
    elif user_choice > 50 or user_choice < 0 :
        print ("You muse insert number between 0 and 50")
    elif user_choice > pc_choice:
        print ("You nember is too high")
    elif user_choice < pc_choice:
        print ("You nember is too low!")
    elif  user_choice == str:
        print ("Please insert valid number")    
    else :
        print ("Please insert valid number")