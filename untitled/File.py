import random
def generate_password(lenght):
    f = []
    while len(f) < lenght:
        f += random.choice('QWERTYUIOPASDFGHJKLZXCVBNM9')
    return ''.join(f)

def main(n, m):
    passwords = []
    for i in range(n):
        print(generate_password(m))

x = int(input('Сколько Вам нужно паролей?'))
y = int(input('Какой длины будут пароли?'))
main(x, y)