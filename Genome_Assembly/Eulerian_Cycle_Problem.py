def main():
    nodes = []
    edges = {}
    while True:
        inp = input()
        if inp == '':
            break
        inp = inp.split(' -> ')
        in_node = inp[0]
        nodes.append(in_node)
        out_nodes = inp[1].split(',')
        nodes += out_nodes
        if isinstance(out_nodes, list):
            edges[in_node] = out_nodes
        else:
            edges[in_node] = [out_nodes]
    nodes = list(set(nodes))
    start_node = nodes[0]
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
    print("->".join(cycle))


if __name__ == "__main__":
    main()
