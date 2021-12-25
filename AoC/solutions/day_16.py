from mlib.utils import grouper


class Packet:
    """Represents Binary Packet"""

    def __init__(self, hexadecimal: str) -> None:
        self.hex_source = hexadecimal
        self.binary: str = self.toBin(hexadecimal)
        """String with binary value"""
        self.cursor: int = 0
        """Current cursor's position"""
        self.version: int = self.get_version()
        """Integer made from first three binary values in packet"""
        self.type_id: int = self.get_type_id()
        """Integer made from second three binary values in packet"""
        self.subpackets = None
        self.value = None
        if self.type_id != 4:
            self.length_type: int = self.get_length_tid()
            """15 for total bits length or 11 for subpackets length"""
            self.length: int = self.get_length()
            """Subpackets length, either total bits or total subpackets"""
            self.subpackets: list[Packet] = self.get_subpackets()
        else:
            self.value: int = self.get_literal()
            """Value representing literal"""

    def toBin(self, hexadecimal: str) -> bin:
        """Converts source Hexadecimal string to Binary string"""
        chars = []
        size = 8
        if len(hexadecimal) % 2:
            hexadecimal = '0'+hexadecimal
            size = 3
        for char in grouper(hexadecimal, 2):
            chars.append(format(int("".join(char), base=16), f"0{size}b"))
        return "".join(chars)

    def get_version(self) -> int:
        """Retrieves version. Moves cursor by 3"""
        version = int(self.binary[self.cursor : self.cursor + 3], base=2)
        self.cursor += 3
        return version

    def get_type_id(self) -> int:
        """Retrieves Type ID. Moves cursor by 3"""
        tid = int(self.binary[self.cursor : self.cursor + 3], base=2)
        self.cursor += 3
        return tid

    def get_literal(self) -> int:
        """Retrieves literal. Moves cursor by 5 for every group in packet"""
        literal = ""
        for group in grouper(self.binary[self.cursor :], 5, "0"):
            literal += "".join(group[1:])
            self.cursor += 5
            if group[0] == "0":
                self.size = self.cursor
                break
        return int(literal, base=2)

    def get_length_tid(self) -> int:
        """Retrieves length type. Moves cursor by 1"""
        if self.binary[self.cursor] == "0":
            self.cursor += 1
            return 15
        self.cursor += 1
        return 11

    def get_length(self) -> int:
        """Retrieves length. Moves cursor by length type"""
        length = int(self.binary[self.cursor : self.cursor + self.length_type], base=2)
        self.cursor += self.length_type
        return length

    def get_subpackets(self) -> list["Packet"]:
        """Retrieves subpackets. #TODO"""
        sub = []
        #if self.length_type == 11:
            #per_packet = len(self.binary[self.cursor:].rstrip('0')) // self.length
            #sub = [Packet(format(int("".join(i), base=2), "02X")) for i in grouper(self.binary[self.cursor:].rstrip('0'), per_packet)]
        #else:
        offset = 0
        while True:
            if self.length_type == 15:
                binary = self.binary[self.cursor + offset:self.cursor + self.length]
            else:
                binary = self.binary[self.cursor + offset:].rstrip('0')
            if not binary:
                break
            binary = format(int(binary, base=2), "02X")
            p = Packet(binary)
            #if False:#p.subpackets:
            #    for _sub in p.subpackets:
            #        sub.append(_sub)
            #    breakpoint
            #    pass # TODO what if packet is another container?
            #else:
            sub.append(p)
            offset += p.cursor
            if self.length - len(sub) <= 0:
                break
            if self.length - offset <= 0:
                break
        return sub


def process_packet(packet: Packet):
    if packet.type_id == 4:
        return packet.value()
    subpackets = []
    for subpacket in packet.subpackets:
        subpackets.append(process_packet(subpacket))
    return subpackets

class Values:
    def __init__(self, version = None, type_id = None, value = None, length_type = None, length = None, subpackets = [], binary=None) -> None:
        self.version = version
        self.type_id = type_id
        self.value = value
        self.length_type = length_type
        self.length = length
        self.subpackets = subpackets

def test_simple():
    TEST_BINARY = {
        "D2FE28": Values(6, 4, 2021, binary="110100101111111000101000"),
        "38006F45291200": Values(1, 6, length_type=15, length=27, subpackets=[Values(value=10), Values(value=20)], binary="00111000000000000110111101000101001010010001001000000000"),
        #"EE00D40C823060": Values(7, 3, length_type=11, length=3, subpackets=[Values(value=1), Values(value=2), Values(value=3)], binary="11101110000000001101010000001100100000100011000001100000"),
        "8A004A801A8002F478": Values(version=4, subpackets=[Values(1, subpackets=[Values(5, subpackets=[Values(6)])])]),
    }

    for b, values in TEST_BINARY.items():
        b = Packet(b)
        assert b.version == values.version, "Version mismatch"
        tid = b.type_id
        if values.type_id:
            assert b.type_id == values.type_id, "Type mismatch"
        if b.type_id == 4:
            assert b.value == values.value, "Literal mismatch"
        else:
            if values.length_type:
                assert b.length_type == values.length_type, "Length Type ID mismatch"
            if values.length:
                assert b.length == values.length, "Length mismatch"
            for x, subpacket in enumerate(values.subpackets):
                if subpacket.value:
                    assert b.subpackets[x].value == subpacket.value, "Subpacket's value mismatch"
                else:
                    assert_nested(b.subpackets[x], subpacket)

def assert_nested(packet: Packet, expected: Values, x:int = 0, y: int = 0):
    assert packet.version == expected.version, f"Subpacket's version mismatch at nest {y} packet {x}"
    if expected.subpackets:
        for sub, subpacket in zip(packet.subpackets, expected.subpackets):
            x += 1
            assert_nested(sub, subpacket, x, y+1)

def recursive_version(packets: list[Packet], versions: list[int]):
    _sub = []
    for sub in packets:
        versions.append(sub.version)
        if sub.subpackets:
            _sub.extend(sub.subpackets)
    if _sub:
        return recursive_version(_sub, versions)
    return versions

def part1(packets) -> int:
    versions = []
    for packet in packets:
        p = Packet(packet)
        for sub in p.subpackets:
            versions.append(sub.version)
        versions.append(p.version)
    return sum(versions)

def part1(packets):
    return sum(recursive_version([Packet(i) for i in packets], []))

def test_part1():
    TEST_VALUES = {
        "8A004A801A8002F478": 16,
        "620080001611562C8802118E34": 12,
        "C0015000016115A2E0802F182340": 23,
        "A0016C880162017C3686B18A3D4780": 31,
    }
    for packet, value in TEST_VALUES.items():
        s = part1([packet])
        print(packet, s)
        assert s == value, "Solution doesn't match expected solution"


test_simple()
test_part1()


# from AoC.utils import get_input
# solve_part1(get_input(16))
