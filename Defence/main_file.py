import time


# x = int(input())
def what(number):
    end = []
    was = []
    strange = []
    for i in number:
        # end.append(was)
        x = i
        tr = True
        while tr:
            if len(was) != len(set(was)):
                tr = False
                # print(x)

            else:
                if x % 2 == 0:
                    x //= 2

                else:
                    x *= 3
                    x -= 1
                    x // 2
                # print(x,i)
                was.append(x)
                strange.append(i)

    # end = end
    print(was)
    print(set(strange))


def resheto(n):
    lis = [True]*n
    for i in range(2,int(n**0.5)+1):
        if lis[i] == True:
            for j in range(2*i,n,i):
                lis[j] = False
    # print(lis)
    nums = []
    for i in range(2,len(lis)):
        if lis[i]:
            nums.append(i)
    return nums

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            # print(i)
            return False
    return True

print(prime(100001))