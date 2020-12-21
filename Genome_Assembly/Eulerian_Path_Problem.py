def main():
    nodes = []
    has_inputs = []
    edges = {}
    adjacency = {}
    while True:
        inp = input()
        if inp == '':
            break
        inp = inp.split(' -> ')
        node = inp[0]
        nodes.append(node)
        out_nodes = inp[1].split(',')
        if not isinstance(out_nodes, list):
            out_nodes = [out_nodes]
        nodes += out_nodes
        edges[node] = out_nodes
        has_inputs += out_nodes
        for out_node in out_nodes:
            if out_node in adjacency.keys():
                adjacency[out_node] += 1
            else:
                adjacency[out_node] = 1

    for node in set(nodes):
        if node in adjacency.keys():
            adjacency[node] += len(edges[node])
        else:
            adjacency[node] = len(edges[node])

    odd_nodes = []
    for k, v in adjacency.items():
        if v % 2 != 0:
            odd_nodes.append(k)

    start_node = None
    for node in odd_nodes:
        if node not in set(has_inputs):
            start_node = node
            odd_nodes.remove(node)
            break
    finish_node = odd_nodes[0]
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
                cycle = cycle[i + 1:] + cycle[0: i + 1]
                break
    print("->".join(cycle))


if __name__ == "__main__":
    main()
