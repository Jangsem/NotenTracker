import datetime

class Note():
    pass

    def __init__(self, wert, year, month, day):
        self.wert = wert
        self.date = datetime.datetime(year, month, day)

    gewicht = 1

    def setWert(self, w):
        self.wert = w

    def getWert(self):
        return self.wert

    def getDate(self):
        return self.date

note1 = Note(5, 2020, 9, 28)
note2 = Note(5.25, 2002, 1, 19)

class Fach():
    def __init__(self, name):
        self.name = name
        self.noten = []

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def add_note(self, note):
        self.noten.append(note)

    def add_note(self, wert, year, month, day):
        newnote = Note(wert, year, month, day)
        self.noten.append(newnote)

    def show_noten(self):
        for note in self.noten:
            print(note.getWert(), note.getDate())

    def average(self):
        sum = 0
        for note in self.noten:
            sum += note.getWert()
        return sum / len(self.noten)

    def wish_note(self, wunsch):
        sum = wunsch * (len(self.noten) + 1)
        for note in self.noten:
            sum -= note.getWert()
        return sum

    def remove_note(self, index):
        self.noten.pop(index-1)


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
        for fach in self.faecher:
            print(fach.getName())

    def average(self):
        sum = 0
        for fach in self.faecher:
            sum += fach.getWert()
        return sum / len(self.faecher)

    def addFach(self, fach):
        self.faecher.append(fach)

    def addFach(self, name):
        newFach = Fach(name)
        self.faecher.append(newFach)

fach1 = Fach("Mathematik")
zeugnis1 = Zeugnis('Tenzin', '19/20')
zeugnis1.addFach(fach1)
zeugnis1.addFach("Deutsch")
zeugnis1.show_faecher()
#fach1.add_note(note1)
#fach1.add_note(note2)
#fach1.add_note(5.3, 2019, 02, 25)
#fach1.show_noten()



