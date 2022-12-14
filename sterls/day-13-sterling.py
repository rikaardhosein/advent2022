from functools import cmp_to_key


def compare(l,r):
    if type(l) == int:
        l = [l]
    if type(r) == int:
        r = [r]
    for l1, r1 in zip(l,r):
        if type(l1) == list or type(r1) == list:
            res = compare(l1,r1)
        else:
            res = r1 - l1
        if res != 0:
            return res
    return len(r) - len(l)


def main():
    with open("test.txt") as f:
        # 'stolen' from the internet. My manual method was bad.

        """
        GPT - 
        The 'eval' function is used to convert a string representation of a list into a list. 
        The code is splitting the file 'f' into lines and then splitting the lines into pairs using 
        '\n\n' as a delimeter. The 'map' function is used to apply the 'eval' function to each line 
        and then the result is put into a list. The list of pairs is stored in the 'pairs' variable.
        """

        pairs = [list(map(eval, x.splitlines())) for x in f.read().split('\n\n')]

        sum = 0
        for idx, pair in enumerate(pairs,1):
            if compare(pair[0],pair[1]) >= 0:
                sum += idx
        print(sum)

        pairs.append([[2]])
        pairs.append([[6]])
        sorted_list = sorted([y for x in pairs for y in x],
                             key=cmp_to_key(compare), reverse=True)
        p2 = 1
        for idx, l in enumerate(sorted_list,1):
            if str(l) == "[2]" or str(l) == "[6]":
                p2 *= idx
        print(p2)

if __name__ == '__main__':
    main()
