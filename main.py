

from random import randint

player = input(" rock (r), paper (p), scissor (s)?")


chosen = randint(1, 3)
print(player, 'vs', end=' ')
# print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if player == computer:
    print("DRAW!!")
if player == 'r' and computer == 's':
    print('Player Wins !')
if player == 'r' and computer == 'p':
    print('Computer Wins !')
if player == 'p' and computer == 'r':
    print('Player Wins !')
if player == 'p' and computer == 's':
    print('Computer Wins !')
if player == 's' and computer == 'r':
    print('Player Wins !')
if player == 's' and computer == 's':
    print('Computer Wins !')
