# assignment: https://adventofcode.com/2022/day/2

from utils import read_input_file

input = read_input_file("2")

opp_lookup = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

you_lookup = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

points_lookup = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "win": 6,
    "draw": 3,
    "loose": 0
}

def play(opp_encrypted, you_encrypted, strategy):
    """Plays and returns with the points you get"""
    opp = opp_lookup.get(opp_encrypted)
    
    if strategy == "1":
        you = you_lookup.get(you_encrypted)

    if strategy == "2":
        if (opp == "scissors" and you_encrypted == "X") or (opp == "paper" and you_encrypted == "Y") or (opp == "rock" and you_encrypted == "Z"):
            you = "paper"
        elif (opp == "paper" and you_encrypted == "X") or (opp == "rock" and you_encrypted == "Y") or (opp == "scissors" and you_encrypted == "Z"):
            you = "rock"
        elif (opp == "rock" and you_encrypted == "X") or (opp == "scissors" and you_encrypted == "Y") or (opp == "paper" and you_encrypted == "Z"):
            you = "scissors"

    pts = points_lookup.get(you)
    if (opp == "scissors" and you == "rock") or (opp == "rock" and you == "paper") or (opp == "paper" and you == "scissors"):
        pts += points_lookup.get("win")
    elif (opp == you):
        pts += points_lookup.get("draw")

    #print(f"{opp=} plays {you=} -> points for you: {pts}")
    
    return pts
    
def count_points(input, strategy):
    """Plays each round and sums the points with"""
    pts = 0
    for round in input:
        opp_enc = round[0]
        your_enc = round[2]
        pts += play(opp_enc, your_enc, strategy)

    return pts

if __name__ == "__main__":
    print(f"Part 1 solution: {count_points(input, strategy='1')}")
    print(f"Part 2 solution: {count_points(input, strategy='2')}")

