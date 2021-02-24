def count_letters(text):
    # TODO: Count the number of letters
    num_letters = 0
    print(num_letters, "letter(s)")
    return num_letters

def count_words(text):
    # TODO: Count the number of words
    num_words = 0
    print(num_words, "word(s)")
    return num_words

def count_sentences(text):
    # TODO: Count the number of sentences
    num_sentences = 0
    print(num_sentences, "sentence(s)")
    return num_sentences


text = input("Text: ")

# TODO: Compute the reading level of the text
# using the number of letters, words, and sentences.
letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

index = 0

# TODO: Print the reading level of the text.
