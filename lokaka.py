b = "да"
while (b == "да"):
    print("добро пожаловать в квест!")
    print("но перед началом напиши свое имя")
    name = input()
    print(f"ты очнулся в комнате и ничего не помнишь, только свое имя, {name}")               #лабиринт
    print("перед тобой дверь, так как выбора больше не было, ты открыл ее и прошел внутрь")
    print('*громкий хлопок!*')
    print("ты обернулся и увидел что дверь сзади захлопнулась")
    print("ты оказался в начале лабиринта")
    print("варианты ответа: пойти налево, пойти направо, просто стоять на месте")
    a = input()
    if (a == "пойти налево"):
        print("ты оказался в тупике и умер от жажды, потому что у Путина часы на правой руке")
        print("вы хотите начать заново? y/n?")
        b = input()
    if (a == "пойти направо"):
        print("поздравляю, ты сделал правильный выбор, это потому что у Путина часы на правой руке")      #ЧАСТЬ С ДЕОЗАВРЕКОМ ЕПТ
        print("перед тобой была красная кнопка")
        print("*клик*")
        print("*звуки шагов*")
        print("к вам подбежал огромный ДиоЗавр и проглотил вас")
        print("*звуки жесткой рвоты*")
        print("ты очнулся в гнезде ДиоЗаврьих детенышей")
        print("вокруг тебя три ДиоЗаврика, что ты будешь с ними делать?")
        print("варианты ответа: ничего, съесть")
        c = input()
        if (c == "съесть"):
            print("ты съел трех ДиоЗаврикок заживо и объелся")
            print("*звуки очень громких шагов*")
            print("КАК ВДРУГ ПЕРЕД ТОБОЙ СО ЗЛЫМ ПОСЛЕ УВИДЕННОГО ЛИЦОМ ПРЕДСТАЛ ОГРОМНЫЙ, СИЛЬНЫЙ И СТРАШНЫЙ, ДИОЗАВР")
            print("ты увидел позади себя хвосты ДиоЗавриков которые не съел потому что они не вкусные, кто то не любит оставшееся тесто от кусочков пиццы, а кто то хвосты")
            print("НОВЫЙ ПРЕДМЕТ В ИНВЕНТАРЕ: Острый хвост ДиоЗаврёнка")
            print("А теперь сражайся с этим монстом!")
            print("варианты ответа: ударить в живот, ударить в шею ")
            dodo = input()
            if (dodo == "ударить в шею"):
                print("ДиоЗавр был смертельно ранен и моментально погиб")
                print(f"{name}: УРА НАКОНЕЦ ТО ОН УМЕР")
                print("ты оглянулся и понял что гнездо находится в поле и лишь вдали виднеется окружающий поле лес")
                print("как вдруг вдалеке ты увидел странную конструкцию")
                print("это было здание сделанное из всего подряд что можно найти в лесу и поле: деревья, палки, камни, земля")
                print(f"{name}: это что Майнкрафт? УРА ЭТО МАЙНКРАФТ ")
                print("после осознания того что это не Майнкрафт ты решил пойти к этой конструкции")
                print("*шаги*")
                print("*много шагов*")
                print(f"{name}: вот черт, как же пить хочется........")
                print("ты наконец дошел до этой конструкции и увидел у входа ОООЧЕНЬ старнное существо, будто слияние человека и динозавра которое стоит в обычной человеческой позе")
                print(f"{name}: я могу зайти в это здание?")
                print("Существо: пропуск с тобой?")
                print(f"{name}: пропуск")
                print("Существо: УБЛЮДОК ГОНИ ПРОПУСК ИЛИ ИДИ ОТСЮДА ПРОЧЬ, ЖИТЬ НАДОЕЛО?")
                print("что ты ответишь: a: я здесь впервые, и не знаю ничего о пропуске. б: что я тебе сделал то?")
                answer1 = input()
                if (answer1 == "а"):    
                    print(f"{name}: Я первый раз в этом месте, а каком пропуске вообще речь?")
                if (answer1 == "б"):
                    print(f"{name}: Да что я вообще тебе сделал? хватит орать и угрожать мне!")
                    print("Существо: ладно убивать не буду...")
            if (dodo == "ударить в живот"):
                print("ДиоЗавр был ранен но умирал со временем, и за это время он успел загрысть тебя")
                print("вы хотите начать заново? y/n?")
                b = input()
        if (c == "ничего"):
                print("ДиоЗаврики напали на тебя и загрызли")
                print("вы хотите начать заново? y/n?")
                b = input()
    if (a == "просто стоять на месте"):
            print("Путин не одобрил твой поступок и ты умер")
            print("вы хотите начать заново? y/n?")
            b = input()
    elif (b == "да"):
            print("")
    elif (b == "нет"):
            print("а ну пока тогда")
    else:
            print("вы неправильно ответили на вопрос.")
