from sys import exit
from Patient import Patient
from Rendez_vous import Rendez_vous



main_msg = '''
    1- Ajouter un Patient
    2- Modifier les information d'un patient
    3- Supprimer un Patient
    4- Ajouter un Rendez-vous
    5- Annuler un Rendez-vous
    6- Afficher la liste des Patients
    7- Afficher la liste des Rendez-Vous
    8- Vider la liste des patients
    9- Vider la liste des rendez-vous
    10- Revenu Total
    11- Reafficher la liste des choix
    12- Quitter
'''

def get_choice():
    choice = input("CHOIX: ")
    while choice not in str(range(1, 13)):
        print("LE CHOIX DOIT ETRES ENTRE 1 ET 12 DE LA LISTE CI DESSUS !")
        choice = input("CHOIX: ")
    return int(choice)



if __name__ == "__main__":
    print("============================================================================")
    print("______------*********======== Cabinet Dentaire ========*********------______")
    print("============================================================================")
    print("Selectionner une choix: ")
    print(main_msg)

    choice = get_choice()
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
            if Patient.__add__(Patient(cin, nom, prenom, date_naiss, num_tel)):
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
        elif choice == 6:
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
        elif choice == 7:
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
                    print("DATE: ",i.date)
                    print("HEURE: ", i.heure)
                    counterr += 1
            else:
                print("LISTE VIDE !\n")
        #vider la liste des patients
        #!!!!!!!!!!!!!!!automatiquement les autres tables seront vides aussi
        elif choice == 8:
            print("\n==============================")
            print("VIDER LA LISTE DES PATIENTS")
            print("==============================")
            if Patient.__empty__(Patient):
                print("LISTE DES PATIENTS MAINTENANT VIDE :)\n")
            else:
                print("ERREUR !")
        elif choice == 9:
            print("\n==============================")
            print("VIDER LA LISTE DES RENDEZ-VOUS")
            print("==============================")
            if Rendez_vous.__empty__(Rendez_vous):
                print("LISTE DES PATIENTS MAINTENANT VIDE :)\n")
            else:
                print("ERRUER !")
        elif choice == 10:
            print("\n==============================")
            print("REVENU TOTAL")
            print("==============================")
            print(Rendez_vous.__rev_total__(Rendez_vous), "\n")
        elif choice == 11:
            print(main_msg)
        elif choice == 12:
            print("A BIENTOT :)")
            exit()


        choice = int(input("CHOIX: "))



#TODO
#liste des rendez-vous pour aujourd'hui
#liste des rendez-vous pour une date 
#vidange des listes !!!! Ref des req SQL (INNER JOIN , LEFT OUTER JOIN)
#organisaton des imports ***
#gestion des erreur !!!
#interface graphique (GUI)