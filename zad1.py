def main():
    global doc
    string = input("Podaj tekst do podzialu: ")
    try:
        doc = open('../../../../Desktop/p/pythonProject1/PJN/PJN6/PoliMorf-0.6.7.tab', 'r', encoding='utf8')
    except FileNotFoundError:
        quit()
    #dictionary = {}
    dictionary = set()
    for line in doc:
        lista = line.split("\t")
        #dictionary[lista[0]] = lista[1]
        dictionary.add(lista[0])
        dictionary.add(lista[1])
        dictionary.add(lista[2])
    # dictionary = ["kota", "jako", "kot", "kocham", "ja"]
    # jakochamkota
    # jako cham kota
    print(maxmatch(string, dictionary))

def maxmatch(string, dictionary):
    if not string:
        return []
    for i in range(len(string), 0, -1):
        word = string[:i]
        remain = string[i:]
        if word in dictionary:
            #print(word)
            #print(remain)
            return [word] + maxmatch(remain, dictionary)
    word = string[0]
    remain = string[1:]
    return [word] + maxmatch(remain, dictionary)

if __name__ == '__main__':
    main()
