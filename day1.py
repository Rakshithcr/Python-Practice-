# takes a sentence and returns a dictionary showing how many times each word appears

words = input("Enter sentence :")

def word_count(txt):
    dis = {}

    sentenc = txt.lower().split()

    for i in sentenc:
        if i in dis:
            dis[i] += 1
        else:
            dis[i] = 1
    return dis

print(word_count(words))