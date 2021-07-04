
f = open('noten.txt', 'a')
f.write("moin")
f.close()
f = open("noten.txt", 'r')
print(f.read())