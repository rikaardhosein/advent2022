def modulo(a, b):
    return a - (b * (a // b))

def throw(monkeys, item, div, m1, m2):
    num_to_append = modulo(item,232792560)
    if modulo(item,div) == 0:
        monkeys[m1].append(num_to_append)
    else:
        monkeys[m2].append(num_to_append)

def main():
    with open("input.txt") as f:
        total_inspections = {}
        total_inspections[0] = 0
        total_inspections[1] = 0
        total_inspections[2] = 0
        total_inspections[3] = 0
        total_inspections[4] = 0
        total_inspections[5] = 0
        total_inspections[6] = 0
        total_inspections[7] = 0
        monkeys = {}
        monkeys[0] = [54,61,97,63,74]
        monkeys[1] = [61, 70, 97, 64, 99, 83, 52, 87]
        monkeys[2] = [60, 67, 80, 65]
        monkeys[3] = [61, 70, 76, 69, 82, 56]
        monkeys[4] = [79, 98]
        monkeys[5] = [72, 79, 55]
        monkeys[6] = [63]
        monkeys[7] = [72, 51, 93, 63, 80, 86, 81]

        for i in range(10000):
            for m in range(8):
                items = monkeys[m]
                total_inspections[m] += len(items)
                for item in items:
                    if m == 0:
                        item = item * 7
                        throw(monkeys, item, 17, 5, 3)
                    elif m == 1:
                        item = item + 8
                        throw(monkeys, item, 2, 7, 6)
                    elif m == 2:
                        item = item * 13
                        throw(monkeys, item, 5, 1, 6)
                    elif m == 3:
                        item = item + 7
                        throw(monkeys, item, 3, 5, 2)
                    elif m == 4:
                        item = item + 2
                        throw(monkeys, item, 7, 0, 3)
                    elif m == 5:
                        item = item + 1
                        throw(monkeys, item, 13, 2, 1)
                    elif m == 6:
                        item = item + 4
                        throw(monkeys, item, 19, 7, 4)
                    elif m == 7:
                        item = item * item
                        throw(monkeys, item, 11, 0, 4)
                monkeys[m] = []

        print(total_inspections)
        ins = list(total_inspections.values())
        ins.sort()
        print(ins[-2] * ins[-1])


if __name__ == '__main__':
    main()