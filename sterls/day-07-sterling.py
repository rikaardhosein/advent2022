class node:
    def __init__(self, n, p=None):
        self.name = n
        self.total_size = 0
        self.parent = p
        self.children = {}


def create_or_return_node(name, parent):
    if name not in parent.children:
        parent.children[name] = node(name, parent)

    return parent.children[name]


def increment_sizeof_dir_and_parents(n, amount):
    temp = n
    temp.total_size += amount
    temp = n.parent
    while temp is not None:
        temp.total_size += amount
        temp = temp.parent


def main():
    with open("input.txt") as f:
        root = node("home")
        curr = root
        while True:
            line = f.readline().strip()

            if len(line) == 0:
                break

            if line[0] == "$":
                if line[2:4] == "cd":
                    line = line[5:]
                    if line == "..":
                        if curr.parent is not None:
                            curr = curr.parent
                        else:
                            curr = root
                    elif line == "/":
                        curr = root
                    else:
                        curr = create_or_return_node(line, curr)
                elif line[2:4] == "ls":
                    while True:
                        pos = f.tell()
                        statements = f.readline().strip()
                        # print(curr.name, statements)
                        if len(statements) == 0 or statements[0] == "$":
                            f.seek(pos)
                            break

                        tokens = statements.split(" ")
                        if tokens[0] != "dir":
                            increment_sizeof_dir_and_parents(curr, int(tokens[0]))

        total_sum = 0
        q = [root]
        size_of_min_dir_to_delete = float("inf")
        space_needed = 30000000 - (70000000 - root.total_size)
        while len(q) != 0:
            n = q.pop()
            for _, child in n.children.items():
                q.append(child)
            if n.total_size <= 100000:
                total_sum += n.total_size
            if n.total_size >= space_needed:
                size_of_min_dir_to_delete = min(n.total_size, size_of_min_dir_to_delete)

        print(total_sum)
        print(size_of_min_dir_to_delete)


if __name__ == "__main__":
    main()
