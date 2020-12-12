def main():
    inputs = []
    while True:
        try:
            inp = input()
            inputs.append(inp)
        except:
            break
    for prefix_pattern in inputs:
        for suffix_pattern in inputs:
            if prefix_pattern[:-1] == suffix_pattern[1:]:
                print("{} -> {}".format(suffix_pattern, prefix_pattern))


if __name__ == '__main__':
    main()
