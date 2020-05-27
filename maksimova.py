import random
def save_robot_Vasya (n):
    print ('тик-так... осталось {}%'.format(n))
    minute=0
    while n-2>=0:
        print ('тик-так... осталось {}%'.format(n-2))
        cat= random.randint(1,100)
        dog = random.randint (1, 100)
        ufo= random.randint (1,100)
        minute+=1
        n=n-2
        if cat<=10:
            print ('Кошка убежала!\nРобот Вася спасен!')
            break
        if dog<=3:
            print ('Собака убежала!\nРобот Вася спасен!')
            break
        if minute==5:
            minute=0
            if ufo<=7:
                print ('тик-так... осталось {}%'.format(n))
                print ('Прилетело НЛО и подзарядило Васю :)')
                n+=50
                if n>100:
                    n=100
        if n<=0:
            print ('Робота спасти не удалось :(')
            break
save_robot_Vasya(100)      
            
        
