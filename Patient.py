import sqlite3
from dbcnx import cnx
#class Patient

class Patient:

    patients = []

    #initialisation
    def __init__(self, cin, nom, prenom, date_de_naiss, num_tel):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
        self.date_naiss = date_de_naiss
        self.num_tel = num_tel
    
    # ajouter un patient
    #pour eviter 'Patient object is not callable'
    #change all self (new Patient) by p
    #change all self (Patient object) by Patient
    def __add__(p):
        '''
        if self.patients.__len__():
            for i in self.patients:
                if i.cin == self.cin:
                    return False
        self.patients.append(self)
        return True
        '''
        date_naissance = sqlite3.Date(int(p.date_naiss.split("-")[2]),int(p.date_naiss.split("-")[1]), int(p.date_naiss.split("-")[0]))
        sql = "INSERT INTO PATIENTS(CIN, NOM, PRENOM, DATE_NAISS, NUM_TEL) VALUES (?,?,?,?,?);"
        try:
            cnx.execute(sql, (str(p.cin), p.nom, p.prenom, date_naissance, p.num_tel))
            cnx.commit()
            Patient.__getall__(Patient)
            return True
        except Exception as e:
            print(e)
            return False
    
    # modifier les infomation d'un passient
    def __edit___(self, pcin,  patient_modif):
        '''
        for i in self.patients:
            if i.cin == pcin:
                self.patients[self.patients.index(i)] = patient_modif
                return True
        return False
        '''
        self.__getall__(self)
        if self.patients:
            for i in self.patients:
                if i.cin == pcin:
                    sql = "UPDATE PATIENTS SET NOM = ?, PRENOM = ?, DATE_NAISS = ?, NUM_TEL=? WHERE CIN=?;"
                    date_naissance = sqlite3.Date(int(patient_modif.date_naiss.split("-")[2]),int(patient_modif.date_naiss.split("-")[1]), int(patient_modif.date_naiss.split("-")[0]))
                    try:
                        cnx.execute(sql, (patient_modif.nom, patient_modif.prenom, date_naissance, patient_modif.num_tel, str(pcin)))
                        cnx.commit()
                        return True
                    except Exception as e:
                        return False
        return False

    # supprimer un patient
    def __delete__(self, ncin):
        '''
        for i in self.patients:
            if i.cin == ncin:
                self.patients.remove(i)
                return True
        return False
        '''
        self.__getall__(self)
        if self.patients:
            for i in self.patients:
                if i.cin == ncin:
                    sql = "DELETE FROM PATIENTS WHERE CIN="+str(ncin)+";"
                    try:
                        cnx.execute(sql)
                        cnx.commit()
                        return True
                    except Exception as e:
                        print(e)
                        return False
        return False

    # vider la liste des patients
    def __empty__(self):
        '''
        self.patients = []
        return True
        '''
        sql = "DELETE FROM PATIENTS;"
        try:
            cnx.execute(sql)
            cnx.commit()
            self.__getall__(self)
            return True
        except Exception as e:
            return False
        
    # get a patient by cin
    def __get__(self, cin):
        self.__getall__(self)
        if self.patients.__len__():
            for i in self.patients:
                if i.cin == cin:
                    return i
        return False

    #get full patients list (important to charge the patients class list everytime CRUD happens)
    def __getall__(self):
        #get patients list from database
        sql = "SELECT * FROM PATIENTS;"
        pats = []
        try:
            cursor = cnx.execute(sql)
            for i in cursor:
                pats.append(self(i[0], i[1], i[2], i[3], i[4]))
            self.patients = pats
        except Exception as e:
            print(e)
        return self.patients

    # return "object" informations (string)
    def __toString__(self):
        return("[CIN: "+str(self.cin)+",NOM: "+self.nom+",PRENOM: "+self.prenom+",DATE_DE_NAISSANCE: "+self.date_naiss+",NUMERO_DE_TELEPHONE: "+self.num_tel+"]")

#import random

#cin = random.randint(10000000,99999999)
#p = Patient(cin, "TESTT", "Testt", "10-12-1996", "+216145254") 
#Patient.__add__(p)