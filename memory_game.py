import os
import time
import random
from score_manager import save_highscore, get_highscore

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_memory_game():
    # Word lists for different difficulty levels
    words = {
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
    display_times = {
        "easy": 7,
        "medium": 5,
        "hard": 3
    }
    
    # Get difficulty level
    while True:
        level = input("Choose difficulty level (easy/medium/hard): ").lower()
        if level in words:
            break
        print("Invalid level! Please choose easy, medium, or hard.")
    
    # Show current high score
    current_highscore = get_highscore(level)
    print(f"\nCurrent high score for {level} level: {current_highscore}")
    
    score = 0
    word_list = words[level]
    display_time = display_times[level]
    
    print(f"\nStarting Memory Game - {level.upper()} level")
    print("Type 'exit' to end the game")
    print(f"Words will be displayed for {display_time} seconds")
    input("\nPress Enter to start...")
    
    while True:
        clear_screen()
        word = random.choice(word_list)
        print(f"\nRemember this word: {word}")
        time.sleep(display_time)
        clear_screen()
        
        guess = input("\nWhat was the word? ").lower()
        
        if guess == "exit":
            break
            
        if guess == word:
            score += 1
            print("Correct! +1 point")
        else:
            score = max(0, score - 1)
            print(f"Wrong! The word was: {word}")
            print("-1 point")
        
        print(f"Current score: {score}")
        input("\nPress Enter to continue...")
    
    # Save high score if achieved
    if save_highscore(level, score):
        print(f"\nNew high score achieved: {score}!")
    else:
        print(f"\nGame Over! Final score: {score}")
        print(f"High score for {level} level: {current_highscore}")
    
    return score

if __name__ == "__main__":
    play_memory_game() 