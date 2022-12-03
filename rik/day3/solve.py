import string

def score(c):
    cset = string.ascii_lowercase + string.ascii_uppercase
    return cset.index(c) + 1

lines = []

with open("input.txt", "r") as f:
    p_sum = 0

    for line in f:
        lines.append(line)
        l = len(line)//2
        k = (set(line[0:l]) & set(line[l:])).pop()
        p_sum += score(k)
        
    print(p_sum)


p_sum = 0
for i in range(0,len(lines), 3):
    k = set(lines[i].rstrip()) & set(lines[i+1].rstrip()) & set(lines[i+2].rstrip())
    p_sum += score(k.pop())

print(p_sum)