import art
import os
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
def deal_card():
    ''' This function deals the card '''
    return random.choice(cards)
def cal_score(hand):
    '''To calculate the score of user's and computer's hand'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) == 21:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
def compare(user_score,computer_score):
    ''' To compare the score and give the result '''
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "House wins"
    elif user_score == 0:
        return "Player wins"
    elif user_score > 21:
        return "You went over, House wins"
    elif computer_score > 21:
        return "House went over, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "House wins"
def play_game():
    is_game_over = False
    os.system('cls')
    print(art.logo)
    player_hand = []
    com_hand = []
    for _ in range(2):
        player_hand.append(deal_card())
        com_hand.append(deal_card())
    print(player_hand)
    while not is_game_over:   
        player_score = cal_score(player_hand)
        com_score = cal_score(com_hand)
        if player_score == 0 or com_score == 0 or player_score>21:
            is_game_over = True
        else:
            choice = input("Do you want the card to be dealt ").lower()
            if choice == 'y':
                card = deal_card()
                player_hand.append(card)
                print(player_hand)
            else:
                is_game_over = True
        player_score = cal_score(player_hand)
        if player_score > 21:
            is_game_over =  True
    while com_score != 0 and com_score < 17:
        com_hand.append(deal_card())
        com_score = cal_score(com_hand)
    os.system('cls')
    print(player_hand)
    print(player_score)
    print(com_score)
    print(compare(player_score,com_score))
while input("Do you want to play game of blackjack? y or n ") == 'y':
    play_game()