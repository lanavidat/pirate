#attack
import random
import os
import time
from system.hero_hit import hero_hit, max_hero_hit
from system.hero.hero_quantity_mob import hero_quantity_mob
from system.hero.hero_quantity_died import hero_quantity_died
from system.hero.mob_name import mob_name, mob_rand_name
from system.random_mob_hp import random_mob_hp, mob_hp
from system.mob_hit import mob_hit, max_mob_hit
from system.lets_go import hero_search, lets_go
from system.hero_next_lvl import hero_next_lvl
from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, hero_died, luck, quantity_mob, gold
from system.hero.hero_info import exper as exp_old
from system.loot import new_gold_from_loot
#from system.hero.hero_info import quantity_mob as  quan_mob_old

all_mob_hits = 0
all_hero_hits = 0

# Проверка на удачу в бою.
def luck_now():
    from system.definition import luck_check
    luck_check()

# Сохранение рендомного значение денег в переменную
def new_gold():
    new_gold = new_gold_from_loot()
    return float(new_gold)

# Чтение и сохранение денег в файле
def new_gold_to_wallet():

    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    g = float(new_gold())
    a["gold"] += g
    q_mob_read.close()

    # запись полученного словаря(полночтью) в файл
    q_mob_write = open("system/hero/hero_char.py", "w")
    q_mob_write.write(str(a))
    q_mob_write.close()


def hero_mob_attack():
    if True:
        def combat():
            mob_rand_name()
            random_mob_hp()
            global all_mob_hits, all_hero_hits

            h = hero_name()
            max_hit = max_hero_hit()
            mob_life_attack = float(mob_hp())
            hero_life = float(life())
            mob_hit()
            max_mob_hit()
            m_max_ht = round(max_mob_hit(), 2)
            sw = 0

# LOOTS
            def loots():
                print ("New experience {: <12}{}".format("", float(exper())))
                hero_next_lvl()
                print ("New money {: <18} {}".format("", new_gold()))
                new_gold_to_wallet()
                print ("New loot:{: <20} construct".format(""))

                print ( line )

# LOGS
            def logs():
                global all_mob_hits, all_hero_hits
                from system.exper import new_exp, exper
            #characteristics
                print ("Health:{: <19}{}".format("", life()))
                print ("Hit:{: <22}{}\n".format("", max_hero_hit()))
                print ("Experience:{: <14}{}/{}".format("", exp_old(),next_lvl()))
                print ("Level:{:<20}{}\n".format("",lvl()))
                print ("Strenght:{:<17}{}".format("",strenght()))
                print ("Agility:{:<18}{}".format("",agility()))
                print ("Luck:{:<21}{}".format("",luck()))
                print ("Wallet:{:<21}{}".format("", round(gold(),2)))

            #statistic
                print ( line )
                print ("Rounds:{: <35} {}".format("",sw))
                print ("Hero rounds:{: <27} construct".format(""))
                print ("Mob ounds:{: <30} construct".format(""))
                print ("Hero damages per round:{: <24} {}".format("", round(all_hero_hits, 2)))
                print ("Mob damages per round:{: <24} {}".format("", round(all_mob_hits,2)))
                print ("Hero's victories:{: <25}{}".format("", quantity_mob()))
                print ("Hero's dies:{: <30}{}".format("", hero_died()))
                all_mob_hits = 0
                all_hero_hits = 0
                print ( line )

#Сюда записывать все логи, которые появились после боя
                def write_logs():
                    pass

            def short_log():
################################################# TEST ################################


                #from system.loot import new_gold_from_loot

                #new_gold_from_loot()



###########################################################################################
                print ("Experience:{: <14}{}/{}".format("", exp_old(),next_lvl()))
                print ("Level:{:<20}{}\n".format("",lvl()))
                print ("Strenght:{:<17}{}".format("",strenght()))
                print ("Agility:{:<18}{}".format("",agility()))
                print ("Luck:{:<21}{}".format("",luck()))
                print ( line )

    # начало боя
            while True:

    # отображает номер строки раунда
                time.sleep(1)
                sw += 1
                hero_hits = 0
                mob_hits = 0

    # кидаем костяшки на инициативу хода между мобом и гг
                line = "{:-^80}".format("-")
                hero_random = random.random()
                mob_random = random.random()
                int_mob_life = round(mob_life_attack, 2)
                int_hero_life = round(hero_life, 2)

    # проверка на инициативу героя
                if hero_random >= mob_random:
                    hero_hits = round(hero_hit(), 2)
                    luck_now()
                    luck_check = luck_now()

    # проверка на удачу в бою
                    if luck_check == True:

    # если удача улыбнулась удар max + random_hit
                        max_hit = max_hero_hit()
                        hero_hits = max_hit + hero_hits
                        hero_hits = round(hero_hits, 2)
                        mob_life_attack -= hero_hits
                        int_mob_life = round(mob_life_attack, 2)
                        int_mob_life = round(mob_life_attack, 2)
                        int_hero_life = round(hero_life, 2)
                        all_hero_hits += max_hit

                        os.system('cls||clear')

                        print ( line )
                        print("{:^7}\nТебе улыбнулись сами боги! {} лупит со всей силы! КРИТ! {}НР.\n".format("",hero_name().title(),hero_hits))
    # рамка #####
                        line = "{:-^80}".format("-")
                        print ( line )
                        print ("{: <20}{} {: ^10}{}{: ^10} {}{: >20}".format("",h.title(),"",sw,"",mob_name().title(),""))
                        print ( line )
                        print ("Health (now/max):        {}/{}{: ^20}{}/{}".format(int_hero_life, life(),"",int_mob_life, mob_hp()))
                        print ("Hit (now/max):           {}/{}{: ^20}{}/{}\n".format(hero_hits ,max_hero_hit(),"",mob_hits, max_mob_hit()))

                        short_log()
    #############

    # обычный удар героя
                    else:
                        mob_life_attack -= hero_hits
                        int_mob_life = round(mob_life_attack, 2)

                        all_hero_hits += hero_hits

                        os.system('cls||clear')

                        print ( line )
    #проверка на попадание героя по мобу
                        if hero_hits == 0.0:
                            print ("\nГерой банально промазал. " + mob_name().title() + " ржет в стороне\n")
                        else:
                            print("\n{} бъет на {}НР\n".format(h.title(), hero_hits))
    # рамка #####
                        print ( line )
                        print ("{: <20}{} {: ^10}{}{: ^10} {}{: >20}".format("",h.title(),"",sw,"",mob_name().title(),""))
                        print ( line )
                        print ("Health (now/max):        {}/{}{: ^20}{}/{}".format(int_hero_life, float(life()),"",int_mob_life, float(mob_hp())))
                        print ("Hit (now/max):           {}/{}{: ^20}{}/{}\n".format(hero_hits ,max_hero_hit(),"",mob_hits, max_mob_hit()))

                        short_log()
    ###############

    # проверка на смерть моба и выдача плюшек
                    if int_mob_life <= 0:
                        from system.exper import new_exp, exper

                        new_exp()
                        hero_quantity_mob()
    #проверка уровня
    # Проверка на победу гг
                        os.system('cls||clear')
                        print ( line )
                        print ("\nГерой победил злобного монстра!{:<80}".format(" ").upper())

                        # head
                        print ( line )
                        print ("{: <20}{} {: ^10}{: ^12}{} {: >20}".format("",h.title(),"","","Victory!!",""))
                        print ( line )

                        loots()
                        logs()

    # запрос на новый бой
                        import signal

                        def timeout_handler(signum, frame):
                            raise TimeoutError()

                        signal.signal(signal.SIGALRM, timeout_handler)

                        def input_timer(note, timeout):
                            signal.alarm(timeout)
                            try:
                                s = input("")
                            except TimeoutError:
                                hero_search()
                            finally:
                                signal.alarm(0)
                            return s
                        print("Ищем нового противника... Для остановки нажми ENTER")

                        input_timer(" ", 8)
                        lets_go()

    #  проверка на инициативу моба
                if hero_random <= mob_random:
                    os.system('cls||clear')
                    mob_hits = round(mob_hit(), 2)
    # запоминает удар моба
                    all_mob_hits += mob_hits

    # удар моба
                    hero_life -= mob_hits
                    int_hero_life = round(hero_life, 2)

    # сообщение про удар моба
                    print ( line )
                    print("\n{: ^50}{} кусает героя на {}HP\n".format("",mob_name().title(),mob_hits))
                    print ( line )
                    print ("{: <20}{} {: ^10}{}{: ^10} {}{: >20}".format("",h.title(),"",sw,"",mob_name().title(),""))
                    print ( line )
                    print ("Health (now/max):        {}/{}{: ^20}{}/{}".format(int_hero_life, float(life()),"",int_mob_life, float(mob_hp())))
                    print ("Hit (now/max):           {}/{}{: ^20}{}/{}\n".format(hero_hits ,max_hero_hit(),"",mob_hits, max_mob_hit()))
                    short_log()

    # проверка на смерть героя
                    if int_hero_life <= 0:
                        os.system('cls||clear')
                        print ( line )
                        print("\n               " + str(h.upper()) + " погиб не выдержав побоев.\n".upper())
                    # head
                        print ( line )
                        print ("{: <20}{} {: ^10}{: ^12}{} {: >20}".format("",h.title(),"","",mob_name().title(),""))
                        print ( line )
                        logs()

    # зачисление еденичку за убийство
                        hero_quantity_died()
                        import signal

                        def timeout_handler(signum, frame):
                            raise TimeoutError()
                        signal.signal(signal.SIGALRM, timeout_handler)

                        def input_timer(note, timeout):
                            signal.alarm(timeout)
                            try:
                                s = input("")
                            except TimeoutError:
                                hero_search()
                            finally:
                                signal.alarm(0)
                            return s

                        print("Ищем нового противника... Для остановки нажми ENTER")
                        input_timer(" ", 8)
                        lets_go()

        combat()
