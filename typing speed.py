import time
import random

# Sample texts to choose from for the typing test
sample_texts = [
    "Typing is a skill that can be improved with practice and patience.",
    "Artificial Intelligence is transforming the world in unexpected ways.",
    "Python is a popular programming language for beginners and experts alike.",
    "Learning how to code is like learning a new language.",
    "The quick brown fox jumps over the lazy dog."
]

def get_random_text():
    return random.choice(sample_texts)

def calculate_wpm(typed_text, elapsed_time):
    words = typed_text.split()
    num_words = len(words)
    wpm = (num_words / elapsed_time) * 60  # Words per minute
    return round(wpm, 2)

def calculate_accuracy(sample_text, typed_text):
    sample_words = sample_text.split()
    typed_words = typed_text.split()

    total_words = len(sample_words)
    correct_words = sum(1 for i, word in enumerate(typed_words) if i < total_words and word == sample_words[i])
    
    accuracy = (correct_words / total_words) * 100
    return round(accuracy, 2)

def typing_test():
    sample_text = get_random_text()
    print("\nTyping Speed Test")
    print("\nType the following text and press Enter when finished:\n")
    print(sample_text)
    
    input("\nPress Enter to start the timer...")
    
    start_time = time.time()
    typed_text = input("\nStart typing:\n")
    end_time = time.time()

    elapsed_time = end_time - start_time
    wpm = calculate_wpm(typed_text, elapsed_time)
    accuracy = calculate_accuracy(sample_text, typed_text)

    print("\n--- Results ---")
    print(f"Time Taken: {round(elapsed_time, 2)} seconds")
    print(f"Words Per Minute (WPM): {wpm}")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_test()
