def main():
    k = int(input())
    input_str = input()
    for i in range(len(input_str) - k + 1):
        print(input_str[i:k + i])


if __name__ == '__main__':
    main()
