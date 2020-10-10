from collections import Counter

szoveg = 'leggyakoribb karaktert tartalmazza'

betukSzama = {}
for karakter in szoveg:
    if karakter in betukSzama:
        betukSzama[karakter] = betukSzama.get(karakter) + 1
    else:
        betukSzama[karakter] = 1

print(betukSzama)
        
topThree = Counter(betukSzama).most_common(3)

for i in topThree: 
    print(i[0]," :",i[1]," ")
