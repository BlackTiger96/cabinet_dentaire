from sys import exit
import os
import time
import datetime
from colorama import init, Fore, Style
from Patient import Patient
from Rendez_vous import Rendez_vous


main_msg = '''
====>  Selectionner un choix: \n
    1- Ajouter un Patient
    2- Modifier les information d'un patient
    3- Supprimer un Patient
    4- Ajouter un Rendez-vous
    5- Annuler un Rendez-vous
    6- Verifier un Rendez-vous
    7- Afficher la liste des Patients
    8- Afficher la liste des Rendez-Vous
    9- Vider la liste des patients
    10- Vider la liste des rendez-vous
    11- Revenu Total
    12- Reafficher la liste des choix
    13- Effacer Tout
    14- Quitter
'''

#time tuple

#0--> year (4 digit)
#1--> month (1-12)
#2--> day (1-31)

#3--> hour (0-23)
#4--> minute (0-59)
#5--> second (0-61)


today = str(time.localtime()[0])+"-0"+str(time.localtime()[1])+"-"+str(time.localtime()[2])
now = str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5])

#check rdv time
#0--> Now
#1--> 1 attendez and return time
#2--> 2 "retard" and return "retard" duration

def get_choice(msg):
    choice = False
    while not choice:
        choice = input(msg)
        try:
            choice = int(choice)
        except Exception as e:
            choice = False
    return choice

def compare_time(t_now, t_rdv):
    rdv_timestamp = datetime.datetime.strptime(t_rdv[0]+" "+t_rdv[1], "%Y-%m-%d %H:%M:%S").timestamp()
    now_timestamp = datetime.datetime.strptime(t_now[0]+" "+t_now[1], "%Y-%m-%d %H:%M:%S").timestamp()
    if rdv_timestamp < now_timestamp:
        return True
    else:
        return False

def pred(text):
    init(convert=True)
    print(Fore.RED + text, end="") 
    print(Style.RESET_ALL)

def pgreen(text):
    init(convert=True)
    print(Fore.GREEN + text, end="") 
    print(Style.RESET_ALL)


if __name__ == "__main__":
    print("============================================================================")
    print("______------*********======== Cabinet Dentaire ========*********------______")
    print("============================================================================\n")
    
    print(" --------------------------")
    print("| AUJOURD'HUI: ", today, "|")
    print(" --------------------------")

    print(" --------------------------")
    print("| MAINTENANT: ", now,"   |")
    print(" --------------------------\n")

    print(main_msg)

    choice = get_choice("CHOIX: ")
    while choice:
        # patients operations
        if choice == 1:
            print("\n==============================")
            print("AJOUTER UN PATIENT:")
            print("==============================")
            cin = int(input("CIN: "))
            nom = input("NOM: ")
            prenom = input("PRENOM: ")
            date_naiss = input("DATE DE NAISSANCE(JJ-MM-AAAA): ")
            num_tel = input("NUMERO DE TELEPHONE: ")
            n_pat = Patient(cin, nom, prenom, date_naiss, num_tel)
            if Patient.__add__(n_pat):
                print("PATIENT AJOUTE :)\n")
            else:
                print("ERREUR: VERIFIER LES INFORMATION !\n")
        elif choice == 2:
            print("\n==============================")
            print("MODIFIER UN PATIENT:")
            print("==============================")
            cin = int(input("CIN: "))
            nom = input("NOM: ")
            prenom = input("PRENOM: ")
            date_naiss = input("DATE DE NAISSANCE(JJ-MM-AAAA): ")
            num_tel = input("NUMERO DE TELEPHONE: ")
            edited_pat = Patient(cin, nom, prenom, date_naiss, num_tel)
            if Patient.__edit___(Patient, cin, edited_pat):
                print("PATIENT MODIFIE :)\n")
            else:
                print("ERREUR: VERIFIER LES INFORMATION !\n")
        elif choice == 3:
            print("\n==============================")
            print("SUPPRIMER UN PATIENT:")
            print("==============================")
            cin = int(input("CIN: "))
            if Patient.__delete__(Patient, cin):
                print("PATIENT SUPPRIME\n")
            else:
                print("ERREUR/ VERIFIER LES INFORMATIONS !\n")
        elif choice == 7:
            print("\n==============================")
            print("LISTE DES PATIENTS: ")
            print("==============================")
            if Patient.__getall__(Patient):
                counter = 1
                for i in Patient.__getall__(Patient):
                    print("------------------------------")
                    print("PATIENT ",counter)
                    print("------------------------------")
                    print("CIN: ",i.cin)
                    print("NOM: ",i.nom)
                    print("PRENOM: ", i.prenom)
                    print("DATE DE NAISSANCE: ", i.date_naiss)
                    print("NUMERO DE TELEPHONE: ", i.num_tel, "\n")
                    counter += 1
            else:
                print("LISTE VIDE !\n")
        #rendez_vous operations
        elif choice == 4:
            print("\n==============================")
            print("AJOUTER UN RENDEZ_VOUS:")
            print("==============================")
            cin = int(input("CIN: "))
            date = input("DATE DU RENDEZ-VOUS(JJ-MM-AAAA): ")
            heure = input("HEURE DU RENDEZ-VOUS(HH:MM): ")
            if Rendez_vous.__add__(Rendez_vous(cin, date, heure), Patient.__getall__(Patient)):
                print("RENDEZ-VOUS AJOUTE :)\n")
            else:
                print("ERREUR: VERIFIER LES INFORMATIONS !\n")
        elif choice == 5:
            print("\n==============================")
            print("ANNULER UN RENDEZ-VOUS: ")
            print("==============================")
            cin = int(input("CIN: "))
            if Rendez_vous.__delete__(Rendez_vous, cin):
                print("RENDEZ-VOUS ANNULE :)\n")
            else:
                print("ERREUR: VERIFIER LES INFORMATION !")
        elif choice == 6:
            print("\n==============================")
            print("VERIFIER UN RENDEZ-VOUS: ")
            print("==============================")
            print("1 ---->AUJOURD'HUI")
            print("2 ---->TOUT")
            print("3 ---->DERNIER")
            _choice = get_choice("CHOIX ---->: ")
            while _choice not in [1,2,3]:
                _choice = get_choice("CHOIX ---->: ")
            if _choice == 1:
                cin = int(input("CIN: "))
                today_rdv = Rendez_vous.__getallbydate__(Rendez_vous, cin, today)
                if today_rdv:
                    print("******************************")
                    print("RENDEZ-VOUS: ")
                    print("******************************")
                    for i in today_rdv:
                        if compare_time([i.date, i.heure], [str(today), str(now)]):
                            pgreen("DATE: "+ i.date)
                            pgreen("HEURE: "+ i.heure)
                            print("------------------------------")
                        else:
                            pred("DATE: "+ i.date)
                            pred("HEURE: "+ i.heure)
                            print("------------------------------")
                else:
                    pred("PATIENT N'EXISTE PAS OU VOUS N'AVEZ PAS UN RENDEZ-VOUS !\n")
            elif _choice == 2:
                cin = int(input("CIN: "))
                all_rdvs = Rendez_vous.__getallbycin__(Rendez_vous, cin)
                if all_rdvs:
                    print("******************************")
                    print("RENDEZ-VOUS: ")
                    print("******************************")
                    for i in all_rdvs:
                        if compare_time([i.date, i.heure], [str(today), str(now)]):
                            pgreen("DATE: "+ i.date)
                            pgreen("HEURE: "+ i.heure)
                            print("------------------------------")
                        else:
                            pred("DATE: "+ i.date)
                            pred("HEURE: "+ i.heure)
                            print("------------------------------")
                else:
                    print("PATIENT N'EXISTE PAS OU VOUS N'AVEZ PAS UN RENDEZ-VOUS !\n")
            elif _choice == 3:
                cin = int(input("CIN: "))
                last_rdv = Rendez_vous.__get__(Rendez_vous, cin)
                if last_rdv:
                    if compare_time([last_rdv.date, last_rdv.heure], [str(today), str(now)]):
                        pgreen("******************************")
                        pgreen("RENDEZ-VOUS: ")
                        pgreen("******************************")
                        pgreen("DATE: "+last_rdv.date)
                        pgreen("HEURE: "+last_rdv.heure)
                        pgreen("------------------------------\n")
                    else:
                        pred("******************************")
                        pred("RENDEZ-VOUS: ")
                        pred("******************************")
                        pred("DATE: "+last_rdv.date)
                        pred("HEURE: "+last_rdv.heure)
                        pred("------------------------------\n")
                else:
                    print("PATIENT N'EXISTE PAS OU VOUS N'AVEZ PAS UN RENDEZ-VOUS !\n")
        elif choice == 8:
            print("\n==============================")
            print("LISTE DES RENDEZ-VOUS: ")
            print("==============================")
            if Rendez_vous.__getallrdv__(Rendez_vous):
                counterr = 1
                for i in Rendez_vous.__getallrdv__(Rendez_vous):
                    patient = Patient.__get__(Patient, i.cin)
                    print("------------------------------")
                    print("RENDEZ-VOUS ",counterr)
                    print("------------------------------")
                    print("******************************")
                    print("PATIENT")
                    print("******************************")
                    print("CIN: ",i.cin)
                    print("NOM: ",patient.nom)
                    print("PRENOM: ", patient.prenom)
                    print("DATE DE NAISSANCE: ", patient.date_naiss)
                    print("NUMERO DE TELEPHONE: ", patient.num_tel)
                    print("******************************")
                    print("INFORMATIONS DU RENDEZ-VOUS")
                    print("******************************")
                    if compare_time([i.date, i.heure], [str(today), str(now)]):
                        pgreen("DATE: "+i.date)
                        pgreen("HEURE: "+ i.heure)
                        print("")
                    else:
                        pred("DATE: "+i.date)
                        pred("HEURE: "+ i.heure)
                        print("")
                    counterr += 1
            else:
                print("LISTE VIDE !\n")
        #vider la liste des patients
        #!!!!!!!!!!!!!!!automatiquement les autres tables seront vides aussi
        elif choice == 9:
            print("\n==============================")
            print("VIDER LA LISTE DES PATIENTS")
            print("==============================")
            if Patient.__empty__(Patient):
                print("LISTE DES PATIENTS MAINTENANT VIDE :)\n")
            else:
                print("ERREUR !")
        elif choice == 10:
            print("\n==============================")
            print("VIDER LA LISTE DES RENDEZ-VOUS")
            print("==============================")
            if Rendez_vous.__empty__(Rendez_vous):
                print("LISTE DES PATIENTS MAINTENANT VIDE :)\n")
            else:
                print("ERRUER !")
        elif choice == 11:
            print("\n==============================")
            print("REVENU TOTAL")
            print("==============================")
            print(Rendez_vous.__rev_total__(Rendez_vous), "\n")
        elif choice == 12:
            print(main_msg)
        elif choice == 13:
            os.system("cls")
        elif choice == 14:
            print("A BIENTOT :)")
            exit()


        choice = get_choice("CHOIX: ")



#TODO
#liste des rendez-vous pour aujourd'hui
#liste des rendez-vous pour une date 
#vidange des listes !!!! Ref des req SQL (INNER JOIN , LEFT OUTER JOIN)
#organisaton des imports ***
#gestion des erreur !!!
#interface graphique (GUI)