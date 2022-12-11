

def main():
    with open("input.txt") as f:
        x = 1
        m = {}
        idx = 1
        for line in f.readlines():
            args = line.split()
            if len(args) == 1:
                m[idx] = x
                idx += 1
                continue

            m[idx] = x
            idx += 1
            x += int(args[1])
            
            m[idx] = x
            idx += 1

        sum = 0
        for i in range(20,221,40):
            print(i, m[i-1])
            sum += (m[i-1]*i)
        print(sum)

        m[0] = 1
        for r in range(6):
            s = ""
            for c in range(40):
                idx = ((r*40) + c)
                if abs(m[idx] - c) <= 1:
                    s += "#"
                else:
                    s += "."
            print(s)
            
if __name__ == "__main__":
    main()
