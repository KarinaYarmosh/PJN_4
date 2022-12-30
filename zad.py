#Byte Pair Encoding

#steps of BPE
#1. Remove all punctuation from the text
#2. Split text into characters (<w> for space)
#Repeat
#3. Count frequency of all bigrams
#4. Merge the most frequent bigram
import re
import string


def deleteInterpunction(text):
    text_replace = text.translate(str.maketrans('', '', string.punctuation))
    return text_replace

def splitToChars(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] == ' ':
            new_text += '<w> '
        if text[i] != ' ':
            new_text += text[i] + ' '
    return new_text.lower()

def textToVocab(text):
    text = text.split()
    return set(text)

def get_bigrams(text):
    bigrams = []
    text = text.replace(' ', '')
    text = text.replace('<w>', ' ')
    for i in range(len(text)-1):
        bigrams.append(text[i] + text[i+1])
    print(bigrams)
    for i in range(len(bigrams)):
        if bigrams[i][0] == ' ':
            print(bigrams[i])
            bigrams[i] = '<w>' + bigrams[i][1]
        if bigrams[i][1] == ' ':
            bigrams[i] = bigrams[i][1] + '<w>'
    return bigrams

def count_bigrams(bigrams):
    bigram_count = {}
    for bigram in bigrams:
        bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
    return bigram_count

def bytePairEncoding(text):
    text = deleteInterpunction(text)
    #vocab =
    while len(text) > 1:
        bigrams = get_bigrams(text)
        bigram_count = count_bigrams(bigrams)
        pair = max(bigram_count, key=bigram_count.get)
        text = merge_vocab(pair, text)
    return text


def merge_vocab(pair, text):
    bigram = re.escape(''.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    text = p.sub(''.join(pair), text)
    return text

text = 'Pospiesz się, pieszy, pospiesz się!'
text = deleteInterpunction(text)
text = splitToChars(text)
bigrams = get_bigrams(text)
bigram_count = count_bigrams(bigrams)
print(bigram_count)
print(len(bigram_count))