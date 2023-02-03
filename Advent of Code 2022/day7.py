f = open("inputs/day7.in")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} ({self.size})"


class Folder:
    def __init__(self, name):
        self.files = []
        self.folders = []
        self.name = name

    def size(self):
        return sum(f.size() for f in self.folders) + sum(f.size for f in self.files)


dirs = {"/": Folder("/")}
cur = []
for line in f:
    if "$ cd" in line:
        _, _, d = line.split()
        if d == "..":
            cur.pop()
        else:
            cur.append(d)
    elif "$ ls" in line:
        pass
    else:
        size, name = line.split()
        path = "/".join(cur)
        if size == "dir":
            f = Folder(name)
            dirs[path].folders.append(f)
            dirs[path + "/" + name] = f
        else:
            size = int(size)
            f = File(name, size)
            dirs[path].files.append(f)

total = sum(dirs[f].size() for f in dirs if dirs[f].size() <= 100000)
print("Part 1:", total)

disk_space = 70000000
update_size = 30000000
space_needed = update_size - (disk_space - dirs["/"].size())

best = dirs["/"].size()
for f in dirs:
    if space_needed <= dirs[f].size() < best:
        best = dirs[f].size()
print("Part 2", best)
