def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)




def anagram2(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    obj = {}

    for letter in s1:
        if letter in obj:
            obj[letter] += 1
        else:
            obj[letter] = 1
    
    for letter in s2:
        if letter in obj:
            obj[letter] -= 1
        else:
            obj[letter] += 1

    for k in obj:
        if obj[k] != 0:
            return False
    
    return True
    
print(anagram2('god','dog'))