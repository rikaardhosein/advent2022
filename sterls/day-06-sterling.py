def find_marker(data, markerLen):
    idx = 0
    while idx <= len(data) - markerLen:
        if len(set(data[idx : idx + markerLen])) == markerLen:
            return idx + markerLen
        idx += 1

    return -1


def main():
    with open("input.txt") as f:
        data = f.read()
        print(find_marker(data, 14))


if __name__ == "__main__":
    main()
