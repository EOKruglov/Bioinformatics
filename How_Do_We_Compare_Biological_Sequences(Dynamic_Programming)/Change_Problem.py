def dpchange(money, coins):
    min_num_coins = [0] * (money + 1)
    for m in range(1, money + 1):
        min_num_coins[m] = 2**64
        for coin in coins:
            if m >= coin:
                if min_num_coins[m - coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coin] + 1
    return min_num_coins[money]


def main():
    money = int(input())
    coins = input().split(',')
    for i, val in enumerate(coins):
        coins[i] = int(val)
    print(dpchange(money, coins))


if __name__ == '__main__':
    main()
