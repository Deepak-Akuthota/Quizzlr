from data import data
from art import logo
from art import vs
import random

def acc(account):
    account_name=account['name']
    account_description=account['description']
    account_country=account['country']
    account_followers=account['follower_count']
    return f"Name : {account_name} , Country : {account_country} , Description : {account_description}"

def forrandom():
    return random.choice(data)

def check_answer(a,b):
    if a['follower_count']>b['follower_count']:
        return a['follower_count']
    else:
        return b['follower_count']


a=forrandom()
b=forrandom()
aa=acc(a)
bb=acc(b)
forward = True
score = 0
print(logo)

while forward:
    print(f"A : {aa} \n \n")
    print(vs,"\n \n")
    print(f"B : {bb} \n \n")
    choice=input("Select on who do u think has more followers in Instagram (Write the letter 'A' or 'B' in capitals:")
    if choice=='A':
        user = a
    elif choice=='B':
        user=b
    else:
        print("wrong input bro")
        
    answer=check_answer(a,b)

    print("\n"*20)
    print(logo)
    if answer==user['follower_count']:
        print("Correct")
        score+=1
        print("\n\nYour score is:",score,"\n \n ")
        aa = bb
        b = forrandom()
        bb=acc(b)

    else:
        print("GAME OVERRR")
        print("\n \n FINAL SCORE:",score,"\n \n ")
        forward = False


