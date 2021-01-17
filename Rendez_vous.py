import sqlite3
from dbcnx import cnx
#class Rendez_vous
class Rendez_vous:
    
    PRIX_SEANCE = 50
    rdvs = []
    seances = []
    caisse = []

    def __init__(self, pcin, date ,heure):
        self.cin = pcin
        self.date = date
        self.heure = heure
    
    def __add__(self, patients):
        '''
        for i in patients:
            if i.cin == self.cin:
                self.rdvs.append(self)
                #compter_seances(rdv.patient)
                #caisse.append([self, remise(rdv.patient.cin)])
                return True
        return False
        '''
        self.__getallrdv__()
        self.__getallseances__()
        if patients:
            for i in patients:
                if i.cin == self.cin:

                    date_rdv = sqlite3.Date(int(self.date.split("-")[2]),int(self.date.split("-")[1]), int(self.date.split("-")[0]))

                    heure_rdv = sqlite3.Time(int(self.heure.split(":")[0]),int(self.heure.split(":")[1]),0)
                    sql = "INSERT INTO RENDEZ_VOUS(CIN, RDV_DATE, HEURE) VALUES(?,?,?);"

                    # check rdv same date and hour before insertion
                    if self.__check_rdv_exist__(date_rdv, heure_rdv):
                        try:
                            cnx.execute(sql, (str(self.cin), date_rdv, str(heure_rdv)))
                            cnx.commit()
                            self.__increment_seances__(self.cin)
                            self.__increment_caisse__()
                            return True
                        except Exception as e:
                            print(e)
                            return False
        return False


    def __delete__(self, cinp):
        '''
        for i in reversed(self.rdvs):
            if i.cin == cinp:
                self.rdvs.remove(i)
                #decomp_seances(get_patient(cinp))
                #prep_caisse(cinp)
                return True
        return False
        '''
        self.__getallrdv__(self)
        self.__getallseances__(self)
        if self.rdvs:
            for i in reversed(self.rdvs):
                if i.cin == cinp:
                    #sql request to delete the last tooked rdv
                    sql = "DELETE FROM RENDEZ_VOUS WHERE cin="+str(cinp)+" and rowid = (SELECT MAX(rowid) FROM RENDEZ_VOUS WHERE CIN="+str(cinp)+");"
                    try:
                        cnx.execute(sql)
                        cnx.commit()
                        self.__decrement_seances__(self,cinp)
                        self.__decrement_caisse__(self,cinp)
                        self.__getallrdv__(self)
                        return True
                    except Exception as e:
                        print(e)
                        return False
        return False

    # charge class seances list before incrementation
    def __increment_seances__(self, pcin):
        '''
        if self.seances.__len__():
            for i in self.seances:
                if i[0] == pcin:
                    i[1] += 1
                else:
                    self.seances.append([pcin, 1])
        else:
            self.seances.append([cin, 1])
        '''
        # False mean that class seances list is empty and True is the opposite
        self.__getallseances__()
        sql_req = False
        if self.seances:
            for i in self.seances:
                for j in i:
                    if j == pcin:
                        sql_req = True
        if sql_req:
            sql = "UPDATE SEANCES SET SEANCES = SEANCES + 1 WHERE CIN="+str(pcin)+";"
            try:
                cnx.execute(sql)
                cnx.commit()
                return True
            except Exception as e:
                #print("UPDATE ERROR: ",e)
                return False
        else:
            sql = "INSERT INTO SEANCES(CIN, SEANCES) VALUES(?,?);"
            try:
                cnx.execute(sql, (str(pcin), 1))
                cnx.commit()
                self.__getallseances__()
                return True
            except Exception as e:
                #print("INSERT ERROR: ",e)
                return False
        

    #decrement seances
    def __decrement_seances__(self, pcin):
        '''
        if self.seances.__len__():
            for i in self.seances:
                if i[0] == pcin:
                    i[1] -= 1
        '''
        # False mean that class seances list is empty and True is the opposite
        self.__getallseances__(self)
        if self.seances:
            for i in self.seances:
                if i[0] == pcin: 
                    #if seances > 0 then increment
                    if i[1] > 1:
                        sql = "UPDATE SEANCES SET SEANCES = SEANCES - 1 WHERE CIN="+str(pcin)+";"
                        try:
                            cnx.execute(sql)
                            cnx.commit()
                            self.__getallseances__()
                            return True
                        except Exception as e:
                            #print("UPDATE ERROR: ",e)
                            return False
                    #else seances <= 2 the delete
                    else:
                        sql = "DELETE FROM SEANCES WHERE CIN="+str(pcin)+";"
                        try:
                            cnx.execute(sql)
                            cnx.commit()
                            self.__getallseances__()
                            return True
                        except Exception as e:
                            #print("DELETE ERROR: ",e)
                            return False
    #comment
    def __increment_caisse__(self):
        self.__getallseances__()
        self.__getcaisse__()
        sql = "INSERT INTO CAISSE(CIN, RDV_DATE, HEURE, COUT) VALUES(?,?,?,?);"
        self.PRIX_SEANCE = self.__remise__(self.cin)
        try:
            cnx.execute(sql, (str(self.cin), self.date, self.heure, self.PRIX_SEANCE))
            cnx.commit()
            self.__getallseances__()
            self.__getcaisse__()
            return True
        except Exception as e:
            return False
    
    #comment
    def __decrement_caisse__(self, pcin):
        '''
        for i in reversed(caisse):
            if i[1] == pcin:
                self.caisse.remove(i)
                return True
        '''
        self.__getallseances__(self)
        self.__getcaisse__(self)
        sql = "DELETE FROM CAISSE WHERE CIN="+str(pcin)+" and rowid = (SELECT MAX(rowid) FROM CAISSE WHERE CIN="+str(pcin)+");"
        try:
            cnx.execute(sql)
            cnx.commit()
            self.__getcaisse__()
            return True
        except Exception as e:
            return False

    #comment
    def __remise__(self, pcin):
        prix = 50
        for i in self.seances:
            if i[0] == pcin:
                if i[1] > 3:
                    prix  = 40
        return prix

    #comment
    def __rev_total__(self):
        self.__getcaisse__(self)
        somme = 0
        for i in self.caisse:
            somme += int(i[3])
        return somme

    #comment
    def __empty__(self):
        '''
        self.rdvs = []
        return True
        '''
        sql1 = "DELETE FROM RENDEZ_VOUS;"
        sql2 = "DELETE FROM SEANCES;"
        sql3 = "DELETE FROM CAISSE;"
        try:
            cnx.execute(sql1)
            cnx.commit()
            cnx.execute(sql2)
            cnx.commit()
            cnx.execute(sql3)
            cnx.commit()
            self.__getallrdv__(self)
            #after sql language manup
            self.__getallseances__(self)
            self.__getcaisse__(self)
            return True
        except Exception as e:
            print(e)
            return False

    #comment
    def __get__(self, pcin):
        for i in reversed(self.rdvs):
            if i.cin == pcin:
                return i
        return False

    #comment
    def __getallrdv__(self):
        '''
        if self.rdvs:
            return self.rdvs
        else:
            return False
        '''
        sql = "SELECT * FROM RENDEZ_VOUS;"
        try:
            cursor = cnx.execute(sql)
            rd_vs = []
            for i in cursor:
                rd_vs.append(Rendez_vous(i[0], i[1], i[2]))
            self.rdvs = rd_vs
        except Exception as e:
            return False
        return self.rdvs

    # get all seances (cin, seances) !imp => to check before every rdv CRUD
    def __getallseances__(self):
        sql = "SELECT * FROM SEANCES;"
        sncs = []
        try:
            cursor = cnx.execute(sql)
            for i in cursor:
                if not self.seances:
                    sncs.append(list(i))
                else:
                    for j in self.seances:
                        if i[0] == j[0]:
                            j[1] += 1
                    sncs.append(list(i))
            self.seances = sncs
        except Exception as e:
            return False
        return self.seances
    
    #comment
    def __getcaisse__(self):
        sql = "SELECT * FROM CAISSE;"
        cais = []
        try:
            cursor = cnx.execute(sql)
            for i in cursor:
                cais.append(list(i))
            self.caisse = cais
        except Exception as e:
            return False
        return self.caisse

    #verifier l'existance d'un rendez_vous (opur eliminer le redondance)
    def __check_rdv_exist__(self, date, heure):
        if self.rdvs:
            for i in self.rdvs:
                if i.date == str(date) and i.heure == str(heure):
                    return False
        return True

    #comment
    def __toString__():
        return("[CIN: ",self.cin,", DATE: ",self.date,", HEURE: ",self.heure,"]")



