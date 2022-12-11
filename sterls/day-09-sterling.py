def moveT(T, H):
    row_diff = H[0] - T[0]
    col_diff = H[1] - T[1]

    if row_diff == 2 and col_diff == 2:
        T[0] += 1
        T[1] += 1
    elif row_diff == 2 and col_diff == -2:
        T[0] += 1
        T[1] -= 1
    elif row_diff == -2 and col_diff == 2:
        T[0] -= 1
        T[1] += 1
    elif row_diff == -2 and col_diff == -2:
        T[0] -= 1
        T[1] -= 1
    elif row_diff == 2:
        T[0] += 1
        if col_diff == 1:
            T[1] += 1
        elif col_diff == -1:
            T[1] -= 1
    elif row_diff == -2:
        T[0] -= 1
        if col_diff == 1:
            T[1] += 1
        elif col_diff == -1:
            T[1] -= 1
    elif col_diff == 2:
        T[1] += 1
        if row_diff == 1:
            T[0] += 1
        elif row_diff == -1:
            T[0] -= 1
    elif col_diff == -2:
        T[1] -= 1
        if row_diff == 1:
            T[0] += 1
        elif row_diff == -1:
            T[0] -= 1
    return T


def main():
    with open("input.txt") as f:
        H = [0, 0]
        T = [0, 0]
        N = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
             [0, 0], [0, 0]]
        m = set()
        m.add(tuple(N[9]))
        for line in f.readlines():
            d, s = line.split(" ")
            for i in range(int(s)):
                if d == 'R':
                    N[0][0] += 1
                    for j in range(1, 10):
                        N[j] = moveT(N[j], N[j - 1])
                if d == 'L':
                    N[0][0] -= 1
                    for j in range(1, 10):
                        N[j] = moveT(N[j], N[j - 1])
                if d == 'U':
                    N[0][1] += 1
                    for j in range(1, 10):
                        N[j] = moveT(N[j], N[j - 1])
                if d == 'D':
                    N[0][1] -= 1
                    for j in range(1, 10):
                        N[j] = moveT(N[j], N[j - 1])
                m.add(tuple(N[9]))

        print(len(m))


if __name__ == "__main__":
    main()
