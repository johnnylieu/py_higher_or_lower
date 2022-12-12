from random import randint
from game_data import data
from art import logo, vs
import os

def rand_num():
    rand_num1 = randint(0, len(data))
    rand_num2 = randint(0, len(data))
    rand_num3 = randint(0, len(data))

    return rand_num1, rand_num2, rand_num3

def check(a_score, b_score, num1, num2):
    score = 0
    user_selection = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    if user_selection == 'a':
        if a_score > b_score:
            score += 1
            num1 = num2

def ask(num1=rand_num()[0], num2=rand_num()[1], num3=rand_num()[2]):
    if num1 != num2:
        print(logo)
        a_name = data[num1]['name']
        a_score = data[num1]['follower_count']
        a_description = data[num1]['description']
        a_country = data[num1]['country']
        print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")

        print(vs)
        b_name = data[num2]['name']
        b_score = data[num2]['follower_count']
        b_description = data[num2]['description']
        b_country = data[num2]['country']
        print(f"Compare A: {b_name}, a {b_description}, from {b_country}.")

    check(a_score, b_score, num1, num2)

def main():
    if __name__ == "__main__":
        os.system('cls')
        ask()

main()