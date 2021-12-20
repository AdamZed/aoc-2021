from operator import mul
from functools import reduce

def dump(packets):
    import json
    print(json.dumps(packets, indent=2))
    
def parseLiteral(bins, packet, cursor):
    packet['data'], last = 0, False
    while not last:
        last = bins[cursor] == '0'
        packet['data'] = (packet['data'] << 4) | int(bins[cursor+1:cursor+5], 2)
        cursor += 5
    return cursor

def parseOperator(bins, packet, cursor):
    tid_0, cursor = bins[cursor] == '0', cursor + 1
    packet['tid'] = int(tid_0)
    if tid_0:
        bitlen = int(bins[cursor:cursor+15], 2)
        cursor += 15
        packet['packets'] = parsePackets(bins[cursor:cursor+bitlen])
        cursor += bitlen
    else:
        numpa = int(bins[cursor:cursor+11], 2)
        cursor += 11
        packet['packets'] = []
        while numpa > 0:
            p = {}
            cursor = parsePacket(bins, p, cursor)
            packet['packets'].append(p)
            numpa -= 1
    return cursor

def parsePacket(bins, packet, cursor):
    packet['ver'] = int(bins[cursor:cursor+3], 2)
    cursor += 3
    packet['typ'] = int(bins[cursor:cursor+3], 2)
    cursor += 3
    if packet['typ'] == 4:
        cursor = parseLiteral(bins, packet, cursor)
    else:
        cursor = parseOperator(bins, packet, cursor)
    return cursor

def parsePackets(bins):
    cursor = 0
    packets = []
    while cursor < len(bins) - 10:
        packet = {}
        cursor = parsePacket(bins, packet, cursor)
        packets.append(packet)
    return packets

def part1(packets):
    versum = 0
    for p in packets:
        versum += p['ver']
        if 'packets' in p: versum += part1(p['packets'])
    return versum

def part2(packets):
    def value(packet):
        childs = None if 'packets' not in packet else packet['packets']
        match packet['typ']:
            case 0: return sum(value(ch) for ch in childs) 
            case 1: return reduce(mul, (value(ch) for ch in childs))
            case 2: return min(value(ch) for ch in childs) 
            case 3: return max(value(ch) for ch in childs) 
            case 4: return packet['data'] 
            case 5: return int(value(childs[0]) > value(childs[1]))
            case 6: return int(value(childs[0]) < value(childs[1]))
            case 7: return int(value(childs[0]) == value(childs[1]))
            
    return value(packets[0])

def main(fname):
    with open(fname) as f: data = f.read().strip()

    bins = bin(int(data, 16))[2:].zfill(len(data) * 4)
    packets = parsePackets(bins)
    #dump(packets)

    print(f'Part 1: {part1(packets)}')
    print(f'Part 2: {part2(packets)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)