import random
import pymorphy2

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
words = response.content.splitlines()

alphavit = 'йцукенгшщзхъфывапролджэячсмитьбю'
# alphavit = 'езятьсъелщи'
alphavit = sorted([i for i in alphavit])
tr = [[i,0] for i in alphavit]
fls = []

tr = [i for i in tr]
print(tr)





while len(tr) != 1:
    rnd = random.choice(words)
    print(rnd)
    words.remove(rnd)
    x = input()
    for i in rnd:
        for j in tr:
            if x == 'д' and i == j[0] and j[1] >= 0:
                j[1] += 1
                print(j)
            elif x == "н" and i == j[0]:
                tr.remove(j)

n = 1
while n < len(fls):
     for i in range(len(fls)-n):
          if fls[i][1] > fls[i+1][1]:
               fls[i],fls[i+1] = fls[i+1],fls[i]
     n += 1

print(tr[0])