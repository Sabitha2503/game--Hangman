import random

class HangmanCLI:
    def __init__(self):
        self.categories = {
            "fruits": ["apple", "banana", "mango", "grape", "orange", "pineapple", "strawberry", "blueberry", "guava", "kiwi"],
            "animals": ["elephant", "tiger", "giraffe", "kangaroo", "panda", "zebra", "lion", "horse", "rabbit", "pig"],
            "birds": ["parrot", "eagle", "penguin", "sparrow", "peacock", "owl", "flamingo", "crow", "dove"],
            "sports": ["football", "cricket", "tennis", "badminton", "basketball", "hockey", "volleyball", "golf", "boxing"],
            "planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"],
            "trees": ["oak", "pine", "maple", "willow", "mango", "coconut", "baobab", "apple", "neem"],
            "technologies": ["computer", "internet", "software", "hardware", "robotics", "artificial", "blockchain", "cloudcomputing", "edgecomputing"]
        }

        self.attempts_allowed = 7
        self.run_game()

    def choose_category(self):
        print("\nAvailable categories:")
        for category in self.categories:
            print(f"- {category}")
        choice = input("\nEnter a category: ").lower().strip()
        while choice not in self.categories:
            choice = input("Invalid category. Enter again: ").lower().strip()
        return choice

    def run_game(self):
        category = self.choose_category()
        word = random.choice(self.categories[category])
        display = ["_"] * len(word)
        guessed_letters = set()
        attempts = self.attempts_allowed

        print("\n🎮 Hangman Game Started!")
        print(f"Category: {category.capitalize()}")
        print("Word: " + " ".join(display))

        while attempts > 0 and "_" in display:
            guess = input("\nEnter a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single alphabet letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("✅ Good job! Letter is in the word.")
                for i, ch in enumerate(word):
                    if ch == guess:
                        display[i] = guess
            else:
                attempts -= 1
                print(f"❌ Wrong guess! Attempts left: {attempts}")

            print("Word: " + " ".join(display))

        if "_" not in display:
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
        else:
            print(f"\n💀 Game Over! The correct word was: {word}")

if __name__ == "__main__":
    HangmanCLI()
