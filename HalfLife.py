from math import pow
import datetime
from Farma.utils import Maker, MkDict
import os
from os.path import isdir, relpath


class Drug(object):
    """
    This is a class to instantiate a drug object.
    
    Parameters:
    -----------
    path : str
        Path of the folder where the files will be stored.
    half_life : float
        Half life of the drug in hours.
    ta : float
        Time of absorption of the drug in hours.
    
    Attributes:
    -----------
    p_index : int
        Index of the last registered dosage.
    b : str
        Path of the file that stores the drug dosages.
    i : str
        Path of the file that stores the index of the last registered dosage.
    """
    def __init__(self, path: str, half_life: int, ta: int) -> None:
        """ Initialize the class and create the files if they don't exist"""

        self.path = path
        self.dirs = f"{relpath(path)}/date.txt"
        self.i = f"{relpath(path)}/index.txt"
        self.b = f"{relpath(path)}/blevels.txt"
        self.half_life =half_life
        self.p_index = 0
        self.blevels = list()
        self.ta = ta
        self.date = str()
        if isdir(path) != True:
            Maker(path)

        self.ReadFiles()

    def ReadFiles(self):
        """ Read the index and blevels files and return the values as a list"""

        with open(self.dirs, '+r') as f:
            self.date = f.read()

        with open(self.b, '+r') as func:
            st = str(func.read()).split(',')
            self.blevels = [float(x) for x in st]

        with open(self.i, '+r') as f:
            self.p_index = int(f.read())

    def CDate(self) -> int:
        """
        Calculate the difference between two dates and return the difference in hours

        """
        self.ReadFiles()

        date = datetime.datetime.strptime(self.date, "%Y,%m,%d, %H,%M,%S")
        date2 = datetime.datetime.now()

        with open(self.dirs, "w") as f:
            f.write(date2.strftime("%Y,%m,%d, %H,%M,%S"))

        # Calculate the difference between two dates
        diff = date2 - date
        return int(diff.total_seconds()/3600)

    def AddDose(self,dose,var)-> list:

        """ Add a dose to the blevels file and return the new list, interseting the values with the blevels file."""

        dose = int(dose)
        c = int(var)
        base = 1/2
        t = self.CDate()
        list_result = list()
        index = t + self.p_index + c
        pkt = dose/self.ta
        for ts in range(0, self.ta):
            el = pkt*ts
            list_result.append(round(el, 2))

        for tk in range(self.ta, 720):
            el = dose*pow(base, (tk/self.half_life))
            list_result.append(round(el, 2))

        with open(self.i, "+w") as fs:
            fs.write(str(index))

        pdict = MkDict(list_result, index)
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

        return vlist


    def Erase(self):
        """
        Erase and reset all files contents in the folder.
        """
        try:
            reset_path = os.path.join(self.path, "reset.txt")
            with open(reset_path, "r") as reset_file:
                lista = reset_file.read()

            with open(self.b, "w") as f:
                f.write(lista)

            with open(self.i, "w") as s:
                s.write("0")

        except Exception as e:
            print(f"Error while erasing and resetting files: {e}")