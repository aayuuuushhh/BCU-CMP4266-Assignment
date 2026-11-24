# 5.5. Write a function called word frequencies(list_a) that accepts a list of strings
# called list_a and returns a dictionary where the keys are the words from list_a and the
# values are the number of times that word appears in list_a.

def word_frequencies(list_a):
    freq_dict = {}
    for word in list_a:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequencies(words))