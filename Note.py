import datetime
from FileHandler import FileHandler


filehandler = FileHandler()
class Note():
    pass

    def __init__(self, wert, fach, year, month, day):
        self.wert = wert
        self.date = datetime.datetime(year, month, day)
        self.fach = fach


    def setWert(self, w):
        self.wert = w

    def getWert(self):
        return self.wert

    def getDate(self):
        return self.date


class Fach():
    def __init__(self, name):
        self.name = name
        self.noten = []

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name


    def add_note(self, wert, fach, year, month, day):
        filehandler.writeNote(wert, fach, year, month, day)


    def show_noten(self):
        filehandler.readNoten(self.name)

    def average(self):
        filehandler.averageNoten(self.name)

    def wish_note(self, wunsch):
        filehandler.wish(self.name, wunsch)

    def remove_note(self, index):
        self.noten.pop(index-1)

#fach = Fach("mathe")
#fach.average()
#fach.wish_note(5.3)

class Zeugnis:

    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
        self.faecher = []

    def getName(self):
        return self.name

    def getSemester(self):
        return self.semester

    def show_faecher(self):
        return filehandler.readFach()

    def average(self):
        return filehandler.averageFaecher()

    def addFach(self, name):
        filehandler.writeFach(name)

zeugnis = Zeugnis("Tenzin", '1')
print(zeugnis.show_faecher())
zeugnis.average()