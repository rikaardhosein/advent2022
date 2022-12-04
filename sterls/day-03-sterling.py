def find_common_items(s1, s2):
    common_chars = list(set(s1).intersection(s2))
    return common_chars


def get_letter_score(l):
    if l.islower():
        return (1 + ord(l)) - ord('a')
    else:
        return (27 + ord(l)) - ord('A')


def get_total_score(common_items):
    total_score = 0
    for item in common_items:
        total_score += get_letter_score(item)
    return total_score


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f]
        common_items = [
            find_common_items(line[:len(line) // 2], line[len(line) // 2:])[0]
            for line in lines
        ]
        print(get_total_score(common_items))

        idx = 0
        badges = []
        while idx < len(lines) - 2:
            badge = find_common_items(lines[idx], lines[idx + 1])
            badges.append(find_common_items(badge, lines[idx + 2])[0])
            idx += 3
        print(get_total_score(badges))


if __name__ == "__main__":
    main()
