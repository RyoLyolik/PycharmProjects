def just(n):
     h = 0
     for j in range(n+1):
          if j != 0 and n % j == 0:
               h += 1
     if h <= 2:
          return True
     else:
          return False
