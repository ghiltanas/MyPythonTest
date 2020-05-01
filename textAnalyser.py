def countOccurencyInText(s,c):
    count ={}
    for character in s:
        count.setdefault(character,0)
        count[character] = count[character]+1
    return count[c]