# Memory Game

A console-based memory game where players try to remember and recall words. The game features multiple difficulty levels and tracks high scores.

## Features

- Three difficulty levels (Easy, Medium, Hard)
- Different word lists and display times for each level
- High score tracking per difficulty level
- Simple and intuitive console interface

## How to Play

1. Run the game:
   ```bash
   python memory_game.py
   ```

2. Choose a difficulty level:
   - Easy: Simple words (3-5 letters), 7 seconds display time
   - Medium: Moderate words (6-8 letters), 5 seconds display time
   - Hard: Complex words (9+ letters), 3 seconds display time

3. Gameplay:
   - A word will be displayed for a few seconds
   - After the word disappears, type what you remember
   - Get +1 point for correct answers, -1 for incorrect
   - Type 'exit' to end the game

4. High Scores:
   - High scores are saved per difficulty level
   - They persist between game sessions
   - Stored in `highscores.json`

## Future Upgrades

The following features are planned for future versions:
- Text-to-speech for word reading
- Speech recognition for voice input
- Web-based version using Flask
- Additional game modes and challenges

## Requirements

No external dependencies required for the basic version. See `requirements.txt` for optional dependencies for future features. #   m e m o r y - g a m e  
 