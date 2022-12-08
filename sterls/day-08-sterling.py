def getVisScore(mat, row, col):
    r = row - 1
    mul = [0, 0, 0, 0]
    while r >= 0 and mat[row][col] > mat[r][col]:
        mul[0] += 1
        r -= 1
        if r >= 0 and mat[row][col] <= mat[r][col]:
            mul[0] += 1

    r = row + 1
    while r < len(mat) and mat[row][col] > mat[r][col]:
        mul[1] += 1
        r += 1
        if r < len(mat) and mat[row][col] <= mat[r][col]:
            mul[1] += 1

    c = col - 1
    while c >= 0 and mat[row][col] > mat[row][c]:
        mul[2] += 1
        c -= 1
        if c >= 0 and mat[row][col] <= mat[row][c]:
            mul[2] += 1

    c = col + 1
    while c < len(mat[0]) and mat[row][col] > mat[row][c]:
        mul[3] += 1
        c += 1
        if c < len(mat[0]) and mat[row][col] <= mat[row][c]:
            mul[3] += 1

    for i in range(len(mul)):
        mul[i] = max(mul[i], 1)

    res = mul[0] * mul[1] * mul[2] * mul[3]
    return res


def main():
    with open("input.txt") as f:
        mat = []
        r = 0
        for line in f.readlines():
            line = line.strip()
            row = [int(x) for x in line]
            mat.append(row)

        num_visible = (len(mat) + len(mat[0])) * 2 - 4
        vis = {}

        hs = -1
        for r in range(1, len(mat) - 1):
            for c in range(1, len(mat[0]) - 1):
                hs = max(hs, getVisScore(mat, r, c))

        for r in range(1, len(mat) - 1):
            # looking from left
            highest_l = mat[r][0]
            for c in range(1, len(mat[0]) - 1):
                if mat[r][c] > highest_l:
                    vis[(r, c)] = True
                    highest_l = mat[r][c]

            # looking from right
            highest_r = mat[r][-1]
            for c in range(len(mat[0]) - 2, 0, -1):
                if mat[r][c] > highest_r:
                    vis[(r, c)] = True
                    highest_r = mat[r][c]

        for c in range(1, len(mat[0]) - 1):
            # looking from top
            highest_t = mat[0][c]
            for r in range(1, len(mat) - 1):
                if mat[r][c] > highest_t:
                    vis[(r, c)] = True
                    highest_t = mat[r][c]

            # looking from bot
            highest_b = mat[-1][c]
            for r in range(len(mat) - 2, 0, -1):
                if mat[r][c] > highest_b:
                    vis[(r, c)] = True
                    highest_b = mat[r][c]

        # for k in vis.keys():
        #     print(k)
        num_visible += len(vis)
        print(num_visible)

        print(hs)


if __name__ == "__main__":
    main()
