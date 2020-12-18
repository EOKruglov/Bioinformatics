def main():
    k = int(input())
    input_str = input()
    nodes = {}
    k -= 1
    for i in range(len(input_str) - k + 1):
        nodes[input_str[i:k + i]] = []
    for i in range(len(input_str) - k):
        nodes[input_str[i:k + i]] += [input_str[i + 1:k + i + 1]]

    for k, v in nodes.items():
        if v:
            output = "{}".format(k)
            output = output + ' -> ' + ','.join(v)
            print(output)


if __name__ == '__main__':
    main()
