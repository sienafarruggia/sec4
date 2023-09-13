#mon program compte le nombre de mot
#il input un string
#il output un nombre

def count_word(s):
    count0Words = len(s.split())
    return count0Words

print(count_word('count the words in this sentence'))
