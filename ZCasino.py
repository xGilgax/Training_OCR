import random
import math


# print(random.randrange(10))
# print(math.ceil(5.75))

def welcome():
    try:
        start_player_money = int(input(
            'Welcome to the \'-$- How to freely loose your money -$-\' casino!! We are going to play to ROULETTE! How much money do you want to loose?'))
        if start_player_money <= 0:
            print('If you don\'t have any money this place is not for you =)')
            start_player_money = welcome()
    except ValueError:
        print('We take only dollars. No cents or anything else... We talk about real things here!')
        start_player_money = welcome()
    return start_player_money


def start_a_run(player_money):
    bet = betting(player_money)
    player_money = player_money - bet
    bet_number = pick_a_number()
    roll = launch_the_ball()
    player_gain = gain_calculation(bet, roll, bet_number)
    player_money = player_money + player_gain
    return player_money


def betting(player_money):
    try:
        bet = int(input('How much do you want to bet?'))
        if player_money - bet < 0:
            print('You don\'t have that much money. Try again...')
            bet = betting(player_money)
        elif bet <= 0:
            print('You need to bet money to play. Except for loosing money nothing is free here')
            bet = betting(player_money)
    except ValueError:
        print('We take only dollars. No cents or anything else... We talk about real things here!')
        bet = betting(player_money)
    return bet


def pick_a_number():
    try:
        bet_number = int(input('On which number do you want to bet from 0 to 49?'))
        if bet_number < 0 or bet_number > 49:
            print('FROM 0 TO 49... are you blind??')
            bet_number =  pick_a_number()
    except ValueError:
        print('0,1,2,3,...,49. Simple isn\'t it?')
        bet_number = pick_a_number()
    return bet_number


def launch_the_ball():
    roll = random.randrange(50)
    print('The ball stopped on the number :', roll)
    return roll


def gain_calculation(bet, roll, bet_number):
    gain = 0
    if bet_number == roll:
        gain = bet + 3 * bet
        print('Oh you won hard... What a shame... You earned', gain - bet, '$')
    elif parity(bet_number) == parity(roll):
        gain = bet + math.ceil(0.5 * bet)
        print('You hit the right color... What a pity... You earned', gain - bet, '$')
    else:
        print('Nicely done!! You\'re on the good way! You lost', bet, '$')
    return gain


def keep_playing(player_money):
    restart = True
    print('You still have', player_money, '$ to loose!!')
    if player_money <= 0:
        restart = False
        print('Good job!! You lost all your money for free! See you next time =)')
    else:
        try:
            restart = str(input('Do you want to loose more money? (Y/N)'))
        except:
            print('Letters please!!')
        if restart == 'Y' or restart == 'y':
            restart = True
        elif restart == 'N' or restart == 'n':
            restart = False
            print('Really??? If you want to loose money again you know where to find us =)')
        else:
            print('Seems you have some troubles to understand a simple question... Let\'s try again!')
            keep_playing(player_money)
    return restart


def parity(number):
    even = True
    if number % 2 != 0:
        even = False
    return even


restart = True
player_money = welcome()
while restart:
    player_money = start_a_run(player_money)
    restart = keep_playing(player_money)
