''' Mary is a kindergarten teacher . She has given a task to the children after teaching them a list of words. The task is to
find the unknown words (other than the words they already know) from the given text. Write a python function which accepts
the text and the known list of words and returns the set of unknown words found.

Return -1 if there are no unknown words.
Estimated Time - 20 minutes

Sample Input
Text: "the sun rises in the east"
Vocabulary:["sun","in","east","doctor","day"]
Expected Output
{'rises','the'}
'''
def find_unknown_words(text, vocabulary):
    words = text.split()
    unknown_words = set(word for word in words if word not in vocabulary)
    if not unknown_words:
        return -1

    return unknown_words
text = "the sun rises in the east"
vocabulary = ["sun", "in", "east", "doctor", "day"]
unknown_words = find_unknown_words(text, vocabulary)
print(unknown_words)
