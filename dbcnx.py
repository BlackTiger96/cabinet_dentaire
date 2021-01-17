import sqlite3
import os

if not os.path.exists("data"):
    os.mkdir("data")

table_patients = '''
    CREATE TABLE PATIENTS(
        CIN INT PRIMARY KEY NOT NULL,
        NOM TEXT NOT NULL,
        PRENOM TEXT NOT NULL,
        DATE_NAISS DATE NOT NULL,
        NUM_TEL TEXT NOT NULL
    )
'''

table_rdv = '''
    CREATE TABLE RENDEZ_VOUS(
        CIN INT NOT NULL,
        RDV_DATE DATE NOT NULL,
        HEURE TIME NOT NULL,
        FOREIGN KEY(CIN) REFERENCES PATIENTS(CIN)
    )
'''

table_seances = '''
    CREATE TABLE SEANCES(
        CIN INT NOT NULL,
        SEANCES INT NOT NULL,
        FOREIGN KEY(CIN) REFERENCES PATIENTS(CIN)
    )
'''

table_caisse = '''
    CREATE TABLE CAISSE(
        CIN INT NOT NULL,
        RDV_DATE DATE NOT NULL,
        HEURE TIME NOT NULL,
        COUT INT NOT NULL,
        FOREIGN KEY(CIN) REFERENCES PATIENTS(CIN)
    )
'''

cnx = sqlite3.connect("data/cabinet_dentaire.db")

#def create_tables():
try:
    cnx.execute(table_patients)
    cnx.execute(table_rdv)
    cnx.execute(table_seances)
    cnx.execute(table_caisse)
    print("You will see this message only one time !")
    print("Tables Created")
except sqlite3.OperationalError as e:
    pass