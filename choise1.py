def door0():
    print ("Вы просыпаетесь в темной комнате! Что с вами произошло в ы не помните ! Впереди вы видите 2 двери. Выберите одну из них!")
while True:
    

    door = input("> ")

    if door == "1":
        print (" Вы оказываетесь в затопленном подвале. В другом конце комнате вы видите железную дверь, а прямо перед ней  свисающий в воду провод, который время от времени коротит. Слева от  вас вы замечаете стелаж забитый какими-то коробками. Над вами распологаются трубы которые скорее всего смогут выдержать ваш вес. Выберите дальнейшие действия (1 - стелаж; 2 - трубы; 3 - вернууться в комнату, 4 - выйти из игры.) ")
        choose1 = input("> ")
        if choose1 == "1":
            print (" В попытке забраться на стелаж вы задеваете опорную конструкцию и весь стелаж подпет на вас. Вы проиграли!!!")
         if choose1 == "2":
            print (" Забравшись на трубу вы начинаете ползти по ней. Когда вы почти добрались до конца труба начала разваливаться и падать в воду, но в последний момент вы успеваете отпрыгнуть в сторону двери. К сожелению теперь вы не можете вернуться назад по трубам. Выберите ваши дальнейшие действия (1 - открыть железную дверь, 2 - выдернуть провод из разетки и попробовать вернуться вплавь, ).")
        if choose1 == "3":
            print ("#")
        if choose1 == "4":
            print (" Прощайте!")
            break
