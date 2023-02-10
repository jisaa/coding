f = open("inputs/day16.in")

hex_input = f.readline().strip()

bin_string = bin(int(hex_input, 16))[2:]
while len(bin_string) % 4:
    bin_string = "0" + bin_string


class Packet:
    def find_end(bin_string):
        packet_type = int(bin_string[3:6], 2)
        # print(bin_string, packet_type)
        if packet_type == 4:
            i = 6
            while bin_string[i] == "1":
                i += 5
            return i + 5
        else:
            i = bin_string[6]
            if i == "0":
                return int(bin_string[7:22], 2)
            else:
                t = 22
                while t < len(bin_string):
                    t += Packet.find_end(bin_string[t:])
                return t

    def __init__(self, bin_string):
        self.version = int(bin_string[:3], 2)
        self.packet_type = int(bin_string[3:6], 2)
        self.children = []
        # print(bin_string, self.version, self.packet_type)
        # process children
        if self.packet_type != 4:
            i = bin_string[6]
            if i == "0":
                # next 15 bits are l
                # print('i = 0')
                l = int(bin_string[7:22], 2)
                s = 22
                while s - 22 < l:
                    self.children.append(Packet(bin_string[s:]))
                    i = Packet.find_end(bin_string[s:])
                    if i < 0:
                        break
                    s += i
            else:
                # next 11 bits say number of packets
                # print('i = 1')
                l = int(bin_string[7:18], 2)
                s = 18
                for _ in range(l):
                    self.children.append(Packet(bin_string[s:]))
                    i = Packet.find_end(bin_string[s:])
                    s += i

    def get_version_sum(self):
        version_sum = self.version
        for child in self.children:
            version_sum += child.get_version_sum()
        return version_sum

    def pprint(self, level=0):
        print(" " * level, self.version, self.packet_type, len(self.children))
        for c in self.children:
            c.pprint(level + 1)


root = Packet(bin_string)
print("Part 1:", root.get_version_sum())
