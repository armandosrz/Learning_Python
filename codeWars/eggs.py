def unscramble_eggs(word):
    vowel = ['a','e','i','o','u']
    index = 0
    for x in range(len(word)):
        if word == 'egg':
            return word
        index = word.find('egg', index)
        if index ==-1:
            break
        elif word[index-1] not in vowel:
            if word[index-1] == ' ':
                index += 3
            else:
                word = word.replace('egg','', 1)
                index = 0
                print word
    return word

print(unscramble_eggs('screggameggbeggleggedegg egegggeggsegg'))
