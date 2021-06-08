from .helpers import check_word


def detector(sentence):
    temp = sentence.split()
    return check_word(temp)
