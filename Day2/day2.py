def score_game(game:str) -> int:
    moves = game.split(' ')
    opponent = ord(moves[0].upper()) % 64 #65 is ascii value of capital A
    suggested = ord((moves[1]).upper()) % 87 #88 is ascii value of capital X
    score = suggested
    if (suggested == opponent):
        score += 3
    if (suggested == (opponent % 3 + 1)):
        score += 6
    return score


with open('Day2/input.txt') as f:
    tournament = f.read().splitlines()
    print(sum([score_game(x) for x in tournament]))