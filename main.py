from Art import logo
import random


def choosing(val):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    x = []
    if val == 'Normal':
        for _ in range(2):
            y = random.choice(cards)
            cards.pop(y)
            x.append(y)
        return x
    elif val == 'extra':
        z = random.choice(cards)
        return z



def score(p, c):
    x = input(" \n Do you want to go for extra card. Press Y/N: ")
    if x == 'Y':
       x = choosing('extra')
       print("The extra card you have choosen is : {}".format(x))
       p.append(x)
    if sum(c) < 21:
       x = choosing('extra')
       c.append(x)
    decision(sum(p), sum(c), p, c)


def decision(s_p, s_c, p, c):
    print("Sum of yours cards are : {} \n".format(s_p))
    if s_p == 21 and len(p) == 2:
        print("Congratulations! You Won")
    elif s_p > 21 and s_c > 21:
        print("You Lost")
    elif s_p < 21 and s_c > 21:
        print("Congratulations! You Won")
    elif s_p > s_c and s_p < 21:
        print("You Lost")
    elif s_p < s_c and s_p < 21:
       print("You Lost")




def play_game():
    player = choosing("Normal")
    print("Your Cards are: {} ".format(player))
    computer = choosing("Normal")
    score(player, computer)

if __name__ == "__main__":
    print(logo)
    end_of_game = False
    while end_of_game is not True:
        x = input("Do you want to play BlackJack Game. Press Y/N: \n")
        if x == 'Y':
            play_game()
        elif x == 'N':
            print("Thank You !")
            end_of_game = True
        else:
            print("Please enter correct option")

