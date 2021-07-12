
class FileHandler():
    pass

    def writeNote(self, fach, wert, year, month, day):
        f = open('noten.txt', 'a')
        f.write(str(wert) + " " + str(fach) + " " + str(year)+ " " + str(month)+ " " + str(day)+ "\n")

    def readNoten(self, fach):
        noten = []
        with open('noten.txt', 'r') as file:
            for line in file:
                if (line != ' '):
                    txt = line
                    str = txt.split()
                    if(str[0] == fach):
                        noten.append(str[1] + " " + str[2] + "." + str[3] + "."+ str[4])
        return noten

    def averageNoten(self, fach):
        sum = 0
        count = 0
        with open('noten.txt', 'r') as file:
            for line in file:
                if (line != ' '):
                    txt = line
                    str = txt.split()
                    if (str[0] == fach):
                        count += 1
                        sum+= float(str[1])
        if count == 0:
            return 0
        else:
                average = sum/count
        return round(average, 2)


    def wish(self, fach, wunsch):
        count = 0
        sum = 0
        with open('noten.txt', 'r') as file:
            for line in file:
                if (line != '\n'):
                    txt = line
                    str = txt.split()
                    if (str[0] == fach):
                        count += 1
                        sum+= float(str[1])
        r = (wunsch * (count+1)) - sum
        return round(r,2)

    def writeFach(self, fach):
        f = open('faecher.txt', 'a')
        f.write(fach+"\n")

    def readFach(self):
        faecher = []
        with open('faecher.txt', 'r') as file:
            for line in file:
                if (line != '\n'):
                    faecher.append(line.strip())
        return faecher

    def averageFaecher(self):
        sum = 0
        count = 0
        with open('noten.txt', 'r') as file:
            for line in file:
                if (line != ' '):
                    txt = line
                    str = txt.split()
                    count += 1
                    sum += float(str[1])
        average = sum / count
        return round(average, 2)

    def allNoten(self, fach):
        count = 0
        with open('noten.txt', 'r') as file:
            for line in file:
                if (line != ' '):
                    txt = line
                    str = txt.split()
                    if(str[0] == fach):
                        count+=1
        return count
