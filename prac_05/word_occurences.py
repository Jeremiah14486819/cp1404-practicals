# Program to count word occurrences in a string and display the results in a formatted way
# Time estimate: 20 minutes

# Ask the user for input text
text = input("Text: ")

# Split the text into a list of words
words = text.split()

# Create a dictionary to count the occurrences of each word
word_count = {}

# Loop through the words and update the dictionary
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_count[word] = 1

# Sort the dictionary by the words (keys) alphabetically
sorted_word_count = sorted(word_count.items())

# Find the longest word to align the output properly
max_word_length = max(len(word) for word in word_count)

# Print the word counts with proper formatting
for word, count in sorted_word_count:
    print(f"{word:{max_word_length}} : {count}")
