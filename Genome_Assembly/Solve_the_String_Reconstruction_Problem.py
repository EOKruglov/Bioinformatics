def main():
    k = int(input())
    pattern_lst = []
    while True:
        inp = input()
        if inp == "":
            break
        pattern_lst.append(inp)

    edges = {}
    adjacency = {}
    for pattern in pattern_lst:
        edges[pattern] = []
        adjacency[pattern] = 0

    has_inputs = []
    has_outputs = []

    for suffix_pattern in pattern_lst:
        for prefix_pattern in pattern_lst:
            if suffix_pattern[1:] == prefix_pattern[:-1]:
                edges[suffix_pattern] += [prefix_pattern]
                has_outputs.append(suffix_pattern)
                has_inputs.append(prefix_pattern)
                adjacency[prefix_pattern] += 1
                adjacency[suffix_pattern] += 1

    odd_nodes = []
    for k, v in adjacency.items():
        if v % 2 != 0:
            odd_nodes.append(k)

    [start_node, finish_node] = [odd_nodes[0], odd_nodes[1]] if odd_nodes[0] not in has_inputs or odd_nodes[1] not in \
                                                                has_outputs else [odd_nodes[1], odd_nodes[0]]

    edges[finish_node] += [start_node]

    cycle = [start_node]
    current_node = start_node
    buff_dict = edges.copy()
    while buff_dict:
        if current_node not in buff_dict.keys() or not buff_dict[current_node]:
            for node in cycle:
                if edges[node]:
                    current_node = node
                    cycle = cycle[cycle.index(node):-1] + cycle[0:cycle.index(node)] + [node]
                    break
        next_node = edges[current_node].pop(0)
        if not edges[current_node]:
            buff_dict.pop(current_node)
        cycle.append(next_node)
        current_node = next_node

    if cycle[0] == start_node:
        cycle.pop()
    else:
        for i in range(len(cycle) - 1):
            if cycle[i + 1] == start_node and cycle[i] == finish_node:
                cycle = cycle[i + 1: -1] + cycle[0: i + 1]
                break
    result = cycle[0]
    for pattern in cycle[1:]:
        result += pattern[-1]
    print(result)


if __name__ == "__main__":
    main()
