# Updated Sentence Split Challenge
sentence = "I am a teacher and I love to inspire and teach people."

# 1. Remove the period and convert to lowercase so 'I' matches everything cleanly
clean_sentence = sentence.replace(".", "").lower()

# 2. Split by regular spaces to get clean words
words_list = clean_sentence.split(" ")
print("Words List:", words_list)

# 3. Convert to a set to filter out duplicates
unique_words = set(words_list)
print("Unique Words Set:", unique_words)
print(f"There are {len(unique_words)} unique words in the sentence.")
