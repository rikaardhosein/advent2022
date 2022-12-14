def build_grid(grid, loc1, loc2):
    grid[loc1] = "#"
    for i in range(min(loc1[0], loc2[0]), max(loc1[0], loc2[0]) + 1):
        grid[(i, loc1[1])] = "#"

    for i in range(min(loc1[1], loc2[1]), max(loc1[1], loc2[1]) + 1):
        grid[(loc1[0], i)] = "#"


def print_grid(grid):
    for r in range(170):
        s = ""
        for c in range(70):
            # print(c+494,r)
            if (c + 470, r) not in grid:
                s += "."
            else:
                s += grid[(c + 470, r)]
        print(s)


def get_next_coord(grid, coord, lowest):
    next_coord = [coord[0], coord[1] + 1]

    if next_coord[1] > lowest:
        return None

    # grid[tuple(next_coord)] = 'X'
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord(grid, tuple(next_coord), lowest)

    next_coord[0] -= 1
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord(grid, tuple(next_coord), lowest)

    next_coord[0] += 2
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord(grid, tuple(next_coord), lowest)

    return coord


def get_next_coord2(grid, coord, lowest):
    next_coord = [coord[0], coord[1] + 1]

    grid[coord] = "~"
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord2(grid, tuple(next_coord), lowest)

    next_coord[0] -= 1
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord2(grid, tuple(next_coord), lowest)

    next_coord[0] += 2
    if tuple(next_coord) not in grid or grid[tuple(next_coord)] == "X":
        return get_next_coord2(grid, tuple(next_coord), lowest)

    if next_coord[1] > lowest:
        return None

    return coord


def main():
    with open("input.txt") as f:
        rocks = [
            [tuple(map(eval, tup.split(","))) for tup in rock.strip().split(" -> ")]
            for rock in f.readlines()
        ]

        grid = {}
        grid[(500, 0)] = "+"
        lowest_rock = 0
        for rock in rocks:
            for pebble in range(len(rock) - 1):
                lowest_rock = max(lowest_rock, rock[pebble][1], rock[pebble + 1][1])
                build_grid(grid, rock[pebble], rock[pebble + 1])

        build_grid(grid, (-500, lowest_rock + 2), (9000, lowest_rock + 2))
        lowest_rock += 2
        units = 0
        while True:
            coord = (500, 0)
            next_coord = get_next_coord(grid, coord, lowest_rock)
            # print(coord, next_coord)
            if next_coord is None or next_coord == coord:
                break

            grid[next_coord] = "o"
            units += 1

        print(lowest_rock)
        # get_next_coord2(grid,(500,0),lowest_rock)
        print_grid(grid)
        print(units)


if __name__ == "__main__":
    main()
