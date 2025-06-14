document.addEventListener('DOMContentLoaded', () => {
    // Game state
    let currentLevel = 'medium';
    let currentScore = 0;
    let currentWord = '';
    let gameActive = false;
    let displayTimer = null;

    // DOM elements
    const levelButtons = document.querySelectorAll('[data-level]');
    const gameArea = document.getElementById('game-area');
    const wordDisplay = document.getElementById('current-word');
    const inputArea = document.getElementById('input-area');
    const wordInput = document.getElementById('word-input');
    const submitButton = document.getElementById('submit-guess');
    const startButton = document.getElementById('start-game');
    const endButton = document.getElementById('end-game');
    const scoreDisplay = document.getElementById('current-score');
    const resultMessage = document.getElementById('result-message');

    // Level selection
    levelButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentLevel = button.dataset.level;
            levelButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            gameArea.style.display = 'block';
        });
    });

    // Start game
    startButton.addEventListener('click', () => {
        gameActive = true;
        currentScore = 0;
        scoreDisplay.textContent = currentScore;
        startButton.style.display = 'none';
        endButton.style.display = 'inline-block';
        showNextWord();
    });

    // End game
    endButton.addEventListener('click', () => {
        endGame();
    });

    // Submit guess
    submitButton.addEventListener('click', checkGuess);
    wordInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            checkGuess();
        }
    });

    async function showNextWord() {
        if (!gameActive) return;

        try {
            const response = await fetch('/get_word', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ level: currentLevel })
            });
            const data = await response.json();

            if (data.error) {
                showResult(data.error, 'danger');
                return;
            }

            currentWord = data.word;
            wordDisplay.textContent = currentWord;
            wordDisplay.classList.add('fade-in');
            inputArea.style.display = 'none';
            wordInput.value = '';

            // Clear any existing timer
            if (displayTimer) {
                clearTimeout(displayTimer);
            }

            // Hide word after display time
            displayTimer = setTimeout(() => {
                wordDisplay.classList.remove('fade-in');
                wordDisplay.classList.add('fade-out');
                setTimeout(() => {
                    wordDisplay.textContent = '';
                    wordDisplay.classList.remove('fade-out');
                    inputArea.style.display = 'block';
                    wordInput.focus();
                }, 500);
            }, data.display_time * 1000);

        } catch (error) {
            showResult('Error fetching word. Please try again.', 'danger');
        }
    }

    async function checkGuess() {
        if (!gameActive) return;

        const guess = wordInput.value.trim().toLowerCase();
        if (!guess) return;

        if (guess === currentWord) {
            currentScore++;
            showResult('Correct! +1 point', 'success');
        } else {
            currentScore = Math.max(0, currentScore - 1);
            showResult(`Wrong! The word was: ${currentWord}`, 'danger');
        }

        scoreDisplay.textContent = currentScore;
        showNextWord();
    }

    async function endGame() {
        gameActive = false;
        if (displayTimer) {
            clearTimeout(displayTimer);
        }

        try {
            const response = await fetch('/save_score', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    level: currentLevel,
                    score: currentScore
                })
            });
            const data = await response.json();

            if (data.is_new_highscore) {
                showResult(`New high score achieved: ${currentScore}!`, 'success');
            } else {
                showResult(`Game Over! Final score: ${currentScore}`, 'info');
            }

            // Update high scores display
            document.getElementById('easy-highscore').textContent = data.highscores.easy;
            document.getElementById('medium-highscore').textContent = data.highscores.medium;
            document.getElementById('hard-highscore').textContent = data.highscores.hard;

        } catch (error) {
            showResult('Error saving score. Please try again.', 'danger');
        }

        startButton.style.display = 'inline-block';
        endButton.style.display = 'none';
        inputArea.style.display = 'none';
        wordDisplay.textContent = '';
    }

    function showResult(message, type) {
        resultMessage.textContent = message;
        resultMessage.className = `alert alert-${type}`;
        resultMessage.style.display = 'block';
        setTimeout(() => {
            resultMessage.style.display = 'none';
        }, 3000);
    }
}); 