from markov import *

def trainModel(address: str, prefix: int):
    inFile = open(address, 'r')
    model = Markov(prefix)
    char_obj = []     #its a list of list of characters
    for word in inFile:
        lower_word = word.lower().strip()
        w_char = []
        for char in lower_word:
            w_char.append(char)
           
        w_char.append('$')
        char_obj.append(w_char)

    for obj in char_obj:
        for char in obj:
            model.add(char)

    inFile.close()
    model.reset()
    return model

def generateText(model: Markov, number: int, length: int):
    lst_of_names = []
    while len(lst_of_names) < number: #number of words
        each_word = []
        for _t in range(length): #maximum length of the each word
            next_char = model.randomNext()
            if next_char == '$':
                if len(each_word) > 2:
                    lst_of_names.append(''.join(each_word))
                    break
                else:
                    continue
            else:
                each_word.append(next_char)

    return lst_of_names

