import string
def pig_it(text):
    punc = string.punctuation
    text = text.split(" ")
    for i in range(len(text)):
        if text[i] not in punc:
            temp = text[i][0]
            text[i] = text[i][1:]+temp+"ay"

    return(" ".join(text))
