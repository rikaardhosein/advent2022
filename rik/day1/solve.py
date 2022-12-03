def sum_elf(d):
    d = d.split("\n")
    d = filter(lambda x: len(x) > 0, d)
    d = map(int, d)
    d = sum(d)
    return d

with open("input.txt", "r") as f:
    data = f.read()

    by_elf = data.split("\n\n")
    by_elf = map(sum_elf, by_elf)
    by_elf = list(by_elf)

    print(max(by_elf))
    print(sum(sorted(by_elf)[-3:]))
    





