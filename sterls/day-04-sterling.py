def is_complete_overlap(interval1, interval2):
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
        return True

    if interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
        return True

    return False


def does_overlap_exist(interval1, interval2):
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        return True

    if interval2[0] <= interval1[0] and interval2[1] >= interval1[0]:
        return True

    if interval1[0] <= interval2[1] and interval1[1] >= interval2[1]:
        return True

    if interval2[0] <= interval1[1] and interval2[1] >= interval1[1]:
        return True

    return False


def gpt3_overlap(tuple1, tuple2):
    if tuple1[0] <= tuple2[0]:
        if tuple1[1] >= tuple2[0]:
            return True
        else:
            return False
    else:
        if tuple2[1] >= tuple1[0]:
            return True
        else:
            return False


def gpt3_is_contained(interval1, interval2):
    """
    :param interval1: tuple of two integers
    :param interval2: tuple of two integers
    :return: True if interval1 is contained within interval2, False otherwise
    """
    if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
        return True
    else:
        return False


def main():
    with open("input.txt") as f:
        num_complete_overlap = 0
        num_overlaps = 0
        while line := f.readline().strip():
            intervals = line.split(',')
            interval1 = tuple(map(int, intervals[0].split('-')))
            interval2 = tuple(map(int, intervals[1].split('-')))
            num_complete_overlap += gpt3_is_contained(
                interval1, interval2) or gpt3_is_contained(
                    interval2, interval1)
            num_overlaps += gpt3_overlap(interval1, interval2)

        print(f"{num_complete_overlap=}")
        print(f"{num_overlaps=}")


if __name__ == "__main__":
    main()
