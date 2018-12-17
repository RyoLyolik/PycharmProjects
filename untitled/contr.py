import sys
st = list(map(str.strip, sys.stdin))
st = st[0]
s = st.split()
# sym = list(filter(lambda symbol: not symbol.isalpha(), st))
ss = []
# print(st)
for i in s:
    d = True
    for j in i:
        if j.isalpha() or j.isdigit():
            d= False
    if d:
        ss.append(i)
print(' '.join(ss))