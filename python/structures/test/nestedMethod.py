

# Demonstration of nested functions

# Tuple* of all toy words (for this application)
TOY_WORDS = ('doll', 'car', 'house', 'train')

def concerns_toys(a_sentence):
    # Precondition: a_sentence is a tuple (a list is OK also)
    # Returns whether or not a_sentence contains a word in TOY_WORDS

    def contains_toy_word(a_word):
        # Returns whether or not a_word is in TOY_WORDS
        for toy_word_index in range(0, len(TOY_WORDS)):
            if TOY_WORDS[toy_word_index] in a_word:
                return True
        return False

    for toy_sentence_index in range(0, len(a_sentence)):
        if contains_toy_word(a_sentence[toy_sentence_index]):
            return True
    return False


# Self-tests
# 1
sentence = ('the', 'boy', 'went', 'to', 'town')
result = concerns_toys(sentence)
print("Expect False<-->" + str(result))
# 2
sentence = ('the', 'boy', 'played', 'with', 'his', 'motorcar', 'and', 'cat')
result = concerns_toys(sentence)
print("Expect True<-->" + str(result))