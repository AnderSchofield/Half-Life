from math import pow
from os.path import relpath,isdir
from os import mkdir
import numpy as np
from matplotlib import pyplot as plt

emp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

ix = str(0)

def MkDict(lista, n) -> dict:
    list1 = [x for x in range(n, len(lista))]
    list2 = lista
    new_dict = dict(zip(list1, list2))
    return new_dict

def MAvg(list,period):
    p = int(period)
    sls = []
    i=0
    sl = list[i:11]
    for i in range(p, 382,p):
        s=round(np.sum(sl)/p)
        sl = list[i-p:i]
        sls.append(s)
    return sls

def Maker(path):
    path = str(path)
    mkdir(relpath(path))
    dirs = relpath(path)
    with open(f"{dirs}/blevels.txt", "w") as f:
        f.write(str(emp)[1:-1])
    with open(f"{dirs}/index.txt", "w") as fs:
        fs.write(ix)
    with open(f"{dirs}/reset.txt", "w") as f:
        f.write(str(emp)[1:-1])

class Drug(object):
    """
Drug To be Instanciated with path ans Half_life
    """
    def __init__(self,path, half_life):
        self.path = path
        if isdir(path)!= True:
            Maker(path)
        self.i = relpath(path)+"""/index.txt"""
        self.b = relpath(path) + """/blevels.txt"""
        self.half_life = int(half_life)
        self.p_index = int()
        self.blevels = list()




    def ReadFiles(self):
        with open(self.b, '+r') as func:
            st = str(func.read()).split(',')
            self.blevels = [float(x) for x in st]
        with open(self.i, '+r') as f:
            self.p_index = int(f.read())

    def AddDose(self, dose, t):
        self.ReadFiles()
        base = 1/2;
        t = int(t);
        list_result = list()
        index = t + self.p_index

        for t in range(0, 720):
            el = dose*pow(base, t/ self.half_life)
            list_result.append(round(el, 2))

        with open(self.i, "+w") as fs:
            fs.write(str(index))
        pdict = MkDict(list_result, self.p_index)
        bdict = MkDict(self.blevels, 0)
        bkeys = set(bdict.keys())
        pkeys = set(pdict.keys())
        sum_dict = list()
        for key in set.intersection(bkeys, pkeys):
            nvalue = round((pdict[key] + bdict[key]), 2)
            item = key, nvalue
            sum_dict.append(item)
        for key in set.difference(bkeys, pkeys):
            n2value = round(bdict[key], 2)
            item2 = key, n2value
            sum_dict.append(item2)
        for key in pdict:
            if key not in bdict:
                pass
        sum_dict.sort(key=lambda x: x[0])
        vlist = [z[1] for z in sum_dict]
        with open(self.b, "+w") as f:
            sts = str(vlist)[1:-1]
            f.writelines(sts)
        return  vlist

    def Erase(self):
        try:
            lista = open(relpath(self.path)+"""/reset.txt""", "r").read()
            with open(self.b, "+w") as f:
                sts = str(lista)
                f.writelines(sts)
            with open(self.i, "+w") as s:
                sts = str("0")
                s.writelines(sts)
            print(f"Calculo resetado em {self.path}, Anders!")
        except Exception as e:
            print(f"Erro: {e}")
def Doser(instance : Drug, dose : int, period :int, times : int) -> None:
    for i in range(0,times):
        instance.AddDose(dose,period)



import datetime
from os.path import relpath

if not relpath("date.txt"):
    with open("date.txt", "w") as f:
        f.write("2020,12,12, 12,12,12")

def CDate():
    """
    Calculate the difference between two dates and return the difference in hours

    """
    with open("date.txt", "r") as f:
        sdate = f.read()
    date1 = datetime.datetime.strptime(sdate, "%Y,%m,%d, %H,%M,%S")
    date2 =datetime.datetime.strptime(datetime.datetime.now().strftime("%Y,%m,%d, %H,%M,%S"), "%Y,%m,%d, %H,%M,%S")
    #Calculate the difference between two dates
    diff = date2 - date1  
    with open("date.txt", "w") as f:
        f.write(datetime.datetime.now().strftime("%Y,%m,%d, %H,%M,%S"))
 
    return int(diff.total_seconds()/3600)







l = Drug("lexa", 32)
l2 = Drug("venv", 66)



y = l.blevels
z= l2.blevels
f, (ax,ax2) = plt.subplots(2, 1)
ax.plot(y,'r-')
ax2.plot(z,'b-')

ax.grid(True)
ax.set_xlim([0,(35*t1)])
ax2.grid(True)
plt.show()
l2.Erase()
l.Erase()
