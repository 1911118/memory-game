import json
import os

SCORE_FILE = "highscores.json"

def load_highscores():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"easy": 0, "medium": 0, "hard": 0}
    return {"easy": 0, "medium": 0, "hard": 0}

def save_highscore(level, score):
    highscores = load_highscores()
    if score > highscores.get(level, 0):
        highscores[level] = score
        with open(SCORE_FILE, "w") as f:
            json.dump(highscores, f, indent=4)
        return True
    return False

def get_highscore(level):
    highscores = load_highscores()
    return highscores.get(level, 0) 