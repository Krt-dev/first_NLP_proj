import re


def tokenize_text(text):
    words = []
    current_word = []
    for char in text:
        if char == ' ':
            # masud rani if space ang current char
            if current_word:
                #adds current word to words array
                words.append(''.join(current_word)) 
                #clears the current word array
                current_word = []
        else:
            #mag sge og sulod as long as non space character
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    return words

def white_space_text(text):
    tokenized_text = text.split()
    return tokenized_text

def bigram(text):
    words = text.split()
    bigrams = []
    
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        temp = []
        temp.append(word1)  
        temp.append(word2)  
        bigrams.append(temp)
    
    return bigrams

def trigram(text):
    words = text.split()
    trigrams = []
    
    for i in range(len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]

        temp = []
        temp.append(word1)  
        temp.append(word2)  
        temp.append(word3)

        trigrams.append(temp)
    
    return trigrams

def regex(text):
    
    pattern = r'[\w\']+'
    
  
    sentences = re.findall(pattern, text)
    
    tokenized_sentences = [sentence.split() for sentence in sentences]
    
    return tokenized_sentences

    


def main():
    

    while True:
        text = input("Enter a sentence or paragraph: ")
    
        print("1.) Exit")
        print("2.) White Space")
        print("3.) Bigram")
        print("4.) Trigram")
        print("5.) Regex")

        choice = input("\nWhat would you like to do?")
        choiceInt = int(choice)
        if choiceInt == 1:
            exit()
        elif choiceInt == 2:
            whitespaced = white_space_text(text)
            print("\nResult of White space:")
            for sentence in whitespaced:
                print(sentence)
            #break
        elif choiceInt == 3:
            bigram_word = bigram(text)
            print("\nResult of Bigram:")
            for sentence in bigram_word:
                print(sentence)
            #break
        elif choiceInt == 4:
            trigram_word = trigram(text)
            print("\nResult of Bigram:")
            for sentence in trigram_word:
                print(sentence)
            #break
        elif choiceInt == 5:
            regex_word = regex(text)
            print("\nResult of Regex:")
            print(regex_word)
            # for sentence in regex_word:
            #     print(sentence)
            #break

        

if __name__ == "__main__":
    main()
