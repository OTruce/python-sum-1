import re

# -----------------------------------
# Function 1: Count Specific Word
# -----------------------------------
def count_specific_word(text, search_word):
    if text == "" or search_word == "":
        return 0

    words = re.findall(r"\b\w+\b", text.lower())
    search_word = search_word.lower()

    count = 0

    for word in words:
        if word == search_word:
            count += 1

    return count


# -----------------------------------
# Function 2: Identify Most Common Word
# -----------------------------------
def identify_most_common_word(text):
    if text.strip() == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common = None
    highest_count = 0

    for word in word_counts:
        if word_counts[word] > highest_count:
            highest_count = word_counts[word]
            most_common = word

    return most_common


# -----------------------------------
# Function 3: Average Word Length
# -----------------------------------
def calculate_average_word_length(text):
    if text.strip() == "":
        return 0

    words = re.findall(r"\b\w+\b", text)

    total_length = 0

    for word in words:
        total_length += len(word)

    average = total_length / len(words)

    return float(average)


# -----------------------------------
# Function 4: Count Paragraphs
# -----------------------------------

def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = re.split(r"\n\s*\n", text.strip())

    return len(paragraphs)


# -----------------------------------
# Function 5: Count Sentences
# -----------------------------------

def count_sentences(text):
    if text.strip() == "":
        return 1

    sentences = re.findall(r'[^.!?]+[.!?]', text)

    return len(sentences)



filename = "news-article.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        article = file.read()

except FileNotFoundError:
    print("File not found.")
    article = ""




choice = ""

while choice.lower() != "q":

    print("\nNews Article Analysis")
    print("1. Count specific word")
    print("2. Identify most common word")
    print("3. Average word length")
    print("4. Count paragraphs")
    print("5. Count sentences")
    print("Q. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        word = input("Enter a word to search for: ")
        count = count_specific_word(article, word)
        print(f'"{word}" appears {count} times.')

    elif choice == "2":
        common = identify_most_common_word(article)
        print("Most common word:", common)

    elif choice == "3":
        avg = calculate_average_word_length(article)
        print("Average word length:", round(avg, 2))

    elif choice == "4":
        paragraphs = count_paragraphs(article)
        print("Paragraphs:", paragraphs)

    elif choice == "5":
        sentences = count_sentences(article)
        print("Sentences:", sentences)

    elif choice.lower() == "q":
        print("Program ended.")

    else:
        print("Invalid option.")