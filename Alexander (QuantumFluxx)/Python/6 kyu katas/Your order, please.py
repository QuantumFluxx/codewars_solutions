def order(sentence):
    words = []
    for i in range(1, 10):
        for word in sentence.split(' '):
            if str(i) in word:
                words.append(word)
    return ' '.join(words)