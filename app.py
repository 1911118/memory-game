from flask import Flask, render_template, jsonify, request
import random
import json
import os

app = Flask(__name__)

# Word lists for different difficulty levels
WORDS = {
    "easy": [
        "cat", "dog", "sun", "hat", "run", "big", "red", "box", "cup", "pen",
        "map", "key", "book", "fish", "bird", "tree", "star", "moon", "rain", "snow",
        "ball", "door", "hand", "foot", "head", "eyes", "nose", "ears", "hair", "face",
        "cake", "milk", "rice", "egg", "tea", "coffee", "bread", "meat", "fish", "soup"
    ],
    "medium": [
        "laptop", "python", "rocket", "garden", "window", "bottle", "candle", "pillow", "mirror", "pencil",
        "computer", "keyboard", "monitor", "printer", "speaker", "camera", "phone", "tablet", "screen", "mouse",
        "kitchen", "bedroom", "bathroom", "living", "dining", "office", "school", "hospital", "library", "museum",
        "weather", "climate", "season", "spring", "summer", "autumn", "winter", "morning", "evening", "midnight"
    ],
    "hard": [
        "engineering", "astronomical", "serendipity", "philosophy", "mathematics", "architecture", "technology", "university", "experience", "knowledge",
        "sophisticated", "extraordinary", "revolutionary", "phenomenal", "magnificent", "spectacular", "incredible", "wonderful", "fascinating", "brilliant",
        "environmental", "sustainable", "renewable", "ecological", "biological", "geological", "meteorological", "psychological", "sociological", "anthropological",
        "international", "multinational", "transnational", "intercontinental", "interdisciplinary", "interpersonal", "intercultural", "intergenerational", "interactive", "interconnected"
    ]
}

# Display times for each level (in seconds)
DISPLAY_TIMES = {
    "easy": 7,
    "medium": 5,
    "hard": 3
}

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

@app.route('/')
def index():
    highscores = load_highscores()
    return render_template('index.html', highscores=highscores)

@app.route('/get_word', methods=['POST'])
def get_word():
    level = request.json.get('level', 'medium')
    if level not in WORDS:
        return jsonify({"error": "Invalid level"}), 400
    
    word = random.choice(WORDS[level])
    display_time = DISPLAY_TIMES[level]
    
    return jsonify({
        "word": word,
        "display_time": display_time
    })

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    level = data.get('level')
    score = data.get('score')
    
    if not level or score is None:
        return jsonify({"error": "Missing level or score"}), 400
    
    is_new_highscore = save_highscore(level, score)
    highscores = load_highscores()
    
    return jsonify({
        "is_new_highscore": is_new_highscore,
        "highscores": highscores
    })

if __name__ == '__main__':
    app.run(debug=True) 