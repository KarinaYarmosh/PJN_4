import collections
import string

def main():
    text = 'Pospiesz się, pieszy, pospiesz się!'
    text_replace = text.translate(str.maketrans('', '', string.punctuation))
    text = text_replace
    words = text.split(" ")

    word_dict = collections.defaultdict(int)
    i = len(words)
    for word in words:
        if i == 1:
            word_dict['</w> ' + ' '.join(word) + ' </w>'] += 1
        else:
            word_dict['</w> ' + ' '.join(word)] += 1
            i -= 1

    print(word_dict)

    pairs = collections.defaultdict(int)
    for word, freq in word_dict.items():
        chars = word.split()
        for i in range(len(chars) - 1):
            pairs[chars[i], chars[i + 1]] += freq

    print(pairs)
    print(len(pairs))
    #{<w>, p, o, s, i, e, z, ę, y, <w>p, ie, sz, <w>po, sp, <w>s , ię} - z wykladu - 16 wyrazow

if __name__ == '__main__':
    main()