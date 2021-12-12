from collections import defaultdict, deque

def count_paths(graph, is_part1):
    def dfs(G, edge, path, doubled):
        if edge == "end": return 1
        if edge == "start": return 0
        paths = 0
        for child in G[edge]:
            fresh = child.isupper() or child not in path
            if fresh or not doubled:
                path.append(child)
                paths += dfs(G, child, path, doubled if fresh else True)
                path.pop()
        return paths

    paths = 0
    for edge in graph["start"]:
        paths += dfs(graph, edge, deque([edge]), is_part1)
    return paths

def part1(graph):
    return count_paths(graph, True)

def part2(graph):
    return count_paths(graph, False)

def build_graph(edges):
    G = defaultdict(list)
    for l, r in edges:
        G[l].append(r)
        G[r].append(l)
    return G

def main(fname):
    with open(fname) as f:
        data = [x.strip().split("-") for x in f.readlines() if x != ""]
    
    graph = build_graph(data)

    print(f'Part 1: {part1(graph)}')
    print(f'Part 2: {part2(graph)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)