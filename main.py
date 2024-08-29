from train import *

def main():
    # trainModel(address of the file, size of the prefix)
    my_trained = trainModel('NAMES_M.TXT', 3)

    # generateText(trained model, number of words you want to generate, maximum length of the each generated word )
    result = generateText(my_trained, 1000, 10) 

    print(result)

main()