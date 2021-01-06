#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re
import random

def natGuess():
    import requests
    from bs4 import BeautifulSoup
    import re
    import random

    rounds = 10
    good_answers = 0
    wrong_answers = 0
    user = ""
    used_players = []

    print("\nWitaj w piłkarskim quizie. Twoim zadaniem jest odgadnięcie, z jakiego kraju pochodzi wylosowany przez komputer zawodnik.")
    print("Komputer wybierze dla Ciebie 10 nazwisk. Jeżeli poprawnie dopasujesz wszystkich do danego kraju, zostaniesz piłkarskim mistrzem.")
    print("Powodzenia!")

    user = input("\nZanim zaczniemy, podaj swój nick: ")

    while rounds != 0:
        random_year = random.randint(2000, 2020)

        headers = {'User-Agent': 
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

        page = "https://www.transfermarkt.pl/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id={}".format(random_year)
        pageTree = requests.get(page, headers=headers)
        pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

        Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
        Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

        PlayersList = []
        NatsList = []
        ValuesList = []

        for i in range(0,25):
            PlayersList.append(Players[i].text)
            ValuesList.append(Values[i].text)

        for td in pageSoup.findAll("td", class_="zentriert"):
            inner_grp = []
            for item in td.findAll("img", class_="flaggenrahmen", title=re.compile("^(?!http).*")):
                if item.get('title'):
                    inner_grp.append(item.get('title'))
            if inner_grp:
                NatsList.append(inner_grp)

        random_number = random.randint(0, 24)
        shuffled_player = PlayersList[random_number]
        shuffled_nats = NatsList[random_number]
        shuffled_nats = [word.replace('Stany Zjednaczone','Stany Zjednoczone') for word in shuffled_nats]
        nats_disp = ' i '.join(map(str, shuffled_nats))
        
        while shuffled_player in used_players:
            random_number = random.randint(0, 24)
            shuffled_player = PlayersList[random_number]
            shuffled_nats = NatsList[random_number]
            shuffled_nats = [word.replace('Stany Zjednaczone','Stany Zjednoczone') for word in shuffled_nats]
            nats_disp = ' i '.join(map(str, shuffled_nats))

        print("\nZ jakiego kraju pochodzi", shuffled_player + "?")
        answer = input()
        if answer in shuffled_nats:
            print("Dobra odpowiedź!")
            good_answers += 1
        elif answer == "":
            print("Brak odpowiedzi.")
            if len(shuffled_nats) == 1:
                print(shuffled_player, "pochodzi z kraju", nats_disp)
            if len(shuffled_nats) == 2:
                print(shuffled_player, "jest obywatelem dwóch państw:", nats_disp)
            wrong_answers += 1
        else:
            if len(shuffled_nats) == 1:
                print("Źle. ", shuffled_player, "pochodzi z kraju", nats_disp)
            if len(shuffled_nats) == 2:
                print("Źle. ", shuffled_player, "jest obywatelem dwóch państw:", nats_disp)
            wrong_answers += 1
        used_players.append(shuffled_player)
        rounds -= 1

    if wrong_answers == 0:
        print("Gratulacje", user + ", jesteś piłkarskim mistrzem! Odpowiedziałeś poprawnie na wszystkie pytania.")
    else:
        print("\nWyniki quizu:")
        print("Odpowiedzi poprawnych:", good_answers)
        print("Odpowiedzi niepoprawnych:", wrong_answers)

def guessValue():
    rounds = 10
    good_answers = 0
    wrong_answers = 0

    user = ""

    print("\nWitaj w piłkarskim quizie. Twoim zadaniem jest odgadnięcie, który zawodnik spośród wylosowanej przez komputer pary był więcej wart w danym roku.")
    print("Komputer wybierze dla Ciebie 10 par. Jeżeli prawidłowo wytypujesz danego zawodnika, zostaniesz piłkarskim mistrzem.")
    print("Powodzenia!")

    user = input("\nZanim zaczniemy, podaj swój nick: ")

    while rounds != 0:
        random_number1 = random.randint(0, 24)
        random_number2 = random.randint(0, 24)
        while random_number2 == random_number1:
            random_number2 = random.randint(0, 24)

        random_year = random.randint(2000, 2020)

        headers = {'User-Agent': 
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

        page = "https://www.transfermarkt.pl/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id={}".format(random_year)
        pageTree = requests.get(page, headers=headers)
        pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

        Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
        Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
        Clubs = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})

        PlayersList = []
        ValuesList = []
        ClubsList = []

        for i in range(0,25):
            PlayersList.append(Players[i].text)
            ValuesList.append(Values[i].text)
        
        for i in range(0,50):
            ClubsList.append(Clubs[i].text)
        
        while "" in ClubsList:
            ClubsList.remove("")
        
        shuffled_value1_flt = 0
        shuffled_value2_flt = 0

        while shuffled_value1_flt == shuffled_value2_flt:
            shuffled_player1 = PlayersList[random_number1]
            shuffled_value1 = ValuesList[random_number1]
            shuffled_club1 = ClubsList[random_number1]
            shuffled_value1_flt = float(shuffled_value1.replace("€", "").replace("mln","").replace(" ","").replace(",","."))

            shuffled_player2 = PlayersList[random_number2]
            shuffled_value2 = ValuesList[random_number2]
            shuffled_club2 = ClubsList[random_number2]
            shuffled_value2_flt = float(shuffled_value2.replace("€", "").replace("mln","").replace(" ","").replace(",","."))

        print("Który z tych piłkarzy był więcej warty w", random_year, "roku?")
        print(shuffled_player1, "(" + shuffled_club1 + ")", "[1] vs", shuffled_player2, "(" + shuffled_club2 + ") [2]")
        answer = input()

        if shuffled_value1_flt > shuffled_value2_flt:
            if answer == "1":
                print("\nDobra odpowiedź.")
                good_answers += 1
            elif answer == "2":
                print("\nZła odpowiedź.")
                wrong_answers += 1
            else:
                wrong_answers += 1
        elif shuffled_value1_flt < shuffled_value2_flt:
            if answer == "1":
                print("\nZła odpowiedź.")
                wrong_answers += 1
            elif answer == "2":
                print("\nDobra odpowiedź.")
                good_answers += 1
            else:
                wrong_answers += 1

        print()
        print(shuffled_player1 + ":", shuffled_value1_flt, "mln €")
        print(shuffled_player2 + ":", shuffled_value2_flt, "mln €")
        print()
        rounds -= 1

    if wrong_answers == 0:
        print("Gratulacje", user + ", jesteś piłkarskim mistrzem! Odpowiedziałeś poprawnie na wszystkie pytania.")
    else:
        print("\nWyniki:")
        print("Odpowiedzi poprawnych:", good_answers)
        print("Odpowiedzi niepoprawnych:", wrong_answers)


choice = None
while choice != "0":
    print(
    """
    Quiz piłkarski
    0 - Zakończ
    1 - Z jakiego kraju pochodzę?
    2 - Kto jest więcej wart?
    """
    )
    choice = input("Wybiesz opcję: ")
    print()
    # zakończ
    if choice == "0":
        print("Do widzenia.")
    elif choice == "1":
        natGuess()
    elif choice == "2":
        guessValue()
    else:
        print("\nNiestety,", choice, "to nieprawidłowy wybór.")