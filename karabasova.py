import random

poem = '''Gaudeamus igitur,
Juvenes dum sumus!
Post jugundam juventutem,
Post molestam senectutem
Nos habebit humus.

Ubi sunt, qui ante nos
In mundo fuere?
Vadite ad Superos,
Transite ad Inferos,
Quos si vis videre!

Vita nostra brevis est,
Brevi finietur.
Venit mors velociter,
Rapit nos atrociter,
Nemini parcetur!'''

poem_abst = [i.split('\n') for i in poem.split('\n\n')]
print(poem_abst)

#medium = 5 blanks in abstract
def medium_lvl():
    lines = [len(c) for c in poem_abst]
    print(lines)
    answers = []
    result = []
    not_list = [random.sample([a for a in range(int(i))], int(i) - 5) for i in lines if int(i) > 5]
    print(not_list)
    for m, c in enumerate(poem_abst):
        for i, n in enumerate(c):
            if len(not_list):
                if i != int(not_list[m]):
                    words = n.split(' ')
                    num = random.randint(0, len(words) - 1)
                    while len(words[num]) <= 2:
                        num = random.randint(0, len(words) - 1)
                    answers += [words[num].lower()]
                    words[num] = '______'
                    line = ' '.join(words)
                    print(line)
                    result += [input(' ')]
                else:
                    print(n)
            else:
                words = n.split(' ')
                num = random.randint(0, len(words) - 1)
                while len(words[num]) <= 2:
                    num = random.randint(0, len(words) - 1)
                answers += [words[num].lower()]
                words[num] = '______'
                line = ' '.join(words)
                print(line)
                result += [input(' ')]
    check(answers, result)
    

#easy = blank in every second line
def easy_lvl():
    answers = []
    result = []
    for c in poem_abst:
        i = random.randint(0,1)
        for n in c:
            i += 1
            if i % 2:
                words = n.split(' ')
                num = random.randint(0, len(words) - 1)
                while len(words[num]) <= 2:
                    num = random.randint(0, len(words) - 1)
                answers += [words[num].lower()]
                words[num] = '______'
                line = ' '.join(words)
                print(line)
                result += [input(' ')]
            else:
                print(n)
    check(answers, result)


#checking system
def check(answers, result):
    mistake = {}
    correct = 0
    for i,c in enumerate(answers):
        word = ''
        for letter in c:
            if letter.isalpha() or letter == '-':
                if letter == 'ё': letter = 'е'
                word += letter
        word_ch = result[i].lower()
        word_ch = word_ch.replace('ё', 'е')
        if word_ch == word:
            correct += 1
        else:
            mistake[word_ch] = word
    print('your result: ', correct, '/', len(answers))
    print('your mistakes: (your answer - correct answer)')
    for k,v in mistake.items():
        print(k, '-', v)
        _ = False
        for c in poem_abst:
            for char in c:
                if v in char and not _:
                    print('in "',char,'"')
                    _ = True
                
