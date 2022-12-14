def get_neighbours(mat, curr):
    """
    given a 2D array and a point, return the neighbors of that point
    """
    neighbours = []
    r, c = curr
    if r > 0 and isValid(mat[r - 1][c], mat[r][c]):
        neighbours.append((r - 1, c))
    if r < len(mat) - 1 and isValid(mat[r + 1][c], mat[r][c]):
        neighbours.append((r + 1, c))
    if c > 0 and isValid(mat[r][c-1], mat[r][c]):
        neighbours.append((r, c - 1))
    if c < len(mat[0]) - 1 and isValid(mat[r][c+1], mat[r][c]):
        neighbours.append((r, c + 1))
    return neighbours

def isValid(c1, c2):
    if c1 == 'S':
        c1 = 'a'

    if c2 == 'S':
        c2 = 'a'

    if c1 == 'E':
        c1 = 'z'

    if c2 == 'E':
        c2 = 'z'

    return c1 in [chr(ord(c2)-1), chr(ord(c2)+1), c2]

def main():
    with open("input.txt") as f:
        mat = []
        for line in f.readlines():
            line = line.strip()
            row = [x for x in line]
            mat.append(row)

        end = (0,0)
        start = (0,0)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == "E":
                    end = (row,col)
                if mat[row][col] == "S":
                    start = (row,col)

        print(start, end)
        dp = [[float('inf') for _ in range(len(mat[0]))] for _ in range(len(mat))]

        start, end = end, start
        dp[start[0]][start[1]] = 0
        visited = set()
        visited.add(start)
        q = [start]
        while len(q) > 0:
            l = q.pop()
            ns = get_neighbours(mat,l)
            for n in ns:
                dp[n[0]][n[1]] = min(dp[n[0]][n[1]], 1 + dp[l[0]][l[1]])
                if n not in visited:
                    q.append(n)
                    visited.add(n)

        for row in dp:
            print(row)
        print(dp[end[0]][end[1]])


if __name__ == '__main__':
    main()

