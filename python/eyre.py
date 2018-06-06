# there is a package called nltk. load it for this file.
import nltk

def open_file_and_get_text(filename):
    # given a filename, open it.
    with open(filename, 'r') as our_file:
        # takes the file and reads the text. Stores it.
        text = our_file.read()
    return text

def clean_tokens(words):
    # given some tokens, lowercase them all.
    # create an empty list called clean_words
    clean_words = []

    # loop over every word item in the words list
    for word in words:
        # make each word lowercase and append it to the new list.
        clean_words.append(word.lower())
    return clean_words

# Set a variable filename for where our file is.
our_file = "eyre.txt"

text = open_file_and_get_text(our_file)
# take a long string and break it into words.
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)
# print out first 30 words of our clean tokens
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])
