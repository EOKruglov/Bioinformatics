def main():
    inputs = []
    while True:
        try:
            inp = input()
            inputs.append(inp)
        except:
            break
    result = inputs[0]
    for pattern in inputs[1:]:
        result += pattern[-1]
    print(result)


if __name__ == '__main__':
    main()
