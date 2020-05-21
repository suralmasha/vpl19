def is_palindrome():
    for i in range(len(word) - 1):
        if word[::] == word[:: - 1]:
            print('Your word is a palindrome!')
            return True
        else:
            print('Your word is not a palindrome')
            return False

def how_much_is_palindrome():
    for i in range(len(word) - 1):
    while word[i] == word[- (1 + i)]:
        a += word[i + 2]
        b += word[- (i + 3)]
        part = ''.join(a)
        part2 = ''.join(b[::- 1])
        print('Your word is a `particular` palindrome!\n', part, 'and', part2, 'mirror each other')

def is_particular_palindrome():
    a = []
    b = []
    if word[::] != word[:: - 1]:
        for i in range(len(word) - 1):        
            if word[i] == word[- 1]:
                a += word[i]
                b += word[i]
                if word[i + 1] != word[- 2]:                
                    print('Your word is a `particular` palindrome!\n', a, 'morror each other')
                    return True
                else:
                    how_much_is_palindrome()
                    return True
            else:
                return False


word = input('Input your word: ')
is_palindrome()
if is_palindrome != True:
    is_particular_palindrome()
            
            
            
