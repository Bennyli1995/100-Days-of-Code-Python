############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear
from art import deck, logo
import random

def do_player(player_hand, computer_hand):
    curr = sum(player_hand)
    temp = player_hand
    decision = 'y'

    while decision == 'y':
        decision = input("Type 'y' to get another card, type 'n' to pass: ")
        if (decision == 'n'):
            break
        while (decision == 'y'):
            temp.append(random.choice(deck))
            if (temp[-1] == 11 and sum(temp) > 21):
                curr = sum(temp) - 10
                temp[-1] = 1
            else:
                curr = sum(temp)

            print(f"Your cards: {temp}, current score: {curr}")
            print(f"Computer's first card: {computer_hand[0]}")

            if curr >= 21:
                return temp
            else:
                decision = input(
                    "Type 'y' to get another card, type 'n' to pass: ")

        return temp


def do_computer(computer_hand):
    curr = sum(computer_hand)
    temp = computer_hand
    while curr < 17:
        temp.append(random.choice(deck))
        if (temp[-1] == 11 and sum(temp) > 21):
            curr = sum(temp) - 10
            temp[-1] = 1
        else:
            curr = sum(temp)
    return temp


def compare_hands(computer_hand, player_hand):
    if player_hand == [11, 10] or player_hand == [10, 11]:
        player_score = 0
    else:
        player_score = sum(player_hand)

    if computer_hand == [11, 10] or computer_hand == [10, 11]:
        computer_score = 0
    else:
        computer_score = sum(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(
        f"Computer's final hand: {computer_hand}, final score: {computer_score}"
    )

    if (computer_hand == [11, 10]
            or computer_hand == [10, 11]) and (player_hand == [11, 10]
                                               or player_hand == [10, 11]):
        print("Draw 🙃")
    elif player_hand == [11, 10] or player_hand == [10, 11]:
        print("Win with a Blackjack 😎")
    elif computer_hand == [11, 10] or computer_hand == [10, 11]:
        print("Computer has a blackjack. You lose 😤")
    elif player_score > 21:
        print("You went over. You lose 😤")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif computer_score == player_score:
        print("Draw 🙃")
    elif computer_score < player_score:
        print("You win 😁")
    else:
        print("You lose 😤")


def startGame():
    print(logo)
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if (start == "n"):
        print("Goodbye!")
    else:
        clear()
        player_hand = [random.choice(deck), random.choice(deck)]
        computer_hand = [random.choice(deck)]
        score = 0
        natural = False
        for num in player_hand:
            score += num
        if (score == 21):
          natural = True
          score = 0

        print(f"Your cards: {player_hand}, current score: {score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if score != 0:
            player_hand = do_player(player_hand, computer_hand)

        computer_hand = do_computer(computer_hand)
        print("\n")
        compare_hands(computer_hand, player_hand)

        startGame()

startGame()
