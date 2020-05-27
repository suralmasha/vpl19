
life_truth = ["Юрьевича", "после", "на", "лучший", "Алина", "препод", "земле", "Алексея"]

a = 4

def construction(life_truth, a):
    i_want_you_to_know = []
    start = 0
    copy = life_truth[:]
    while len(life_truth):
        if start % 2:
            i_want_you_to_know.append(copy[a - start])
            life_truth.remove(copy[a - start])
            a = a - start
        else:
            i_want_you_to_know.append(copy[a + start])
            life_truth.remove(copy[a + start])
            a = a + start
        start += 1
    print(" ".join(i_want_you_to_know))
            
construction(life_truth, a)
            
