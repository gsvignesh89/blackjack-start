import random
from art import logo
from replit import clear


def deal_card():
    """Return Random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(nums_list):
    if sum(nums_list) == 21 and len(nums_list) == 2:
        return 0
    
    if 11 in nums_list and sum(nums_list) > 21:
        nums_list.remove(11)
        nums_list.append(1)
    
    return sum(nums_list)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_current_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_current_score}")
        computer_current_score = calculate_score(computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")
        if user_current_score == 0 or computer_current_score == 0 or user_current_score > 21:
            is_game_over = True
        else:
            card_condition = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if card_condition == "y":
                user_cards.append(deal_card())
                print(f"Your cards: {user_cards}, current score: {user_current_score}")
            elif card_condition == "n":
                is_game_over = True
            

    while computer_current_score != 0 and computer_current_score < 17:
        computer_cards.append(deal_card())
        computer_current_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_current_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")
    print(compare(user_score=user_current_score, computer_score=computer_current_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()