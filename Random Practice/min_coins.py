def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    coinCount = 1
    print("They are")
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print("Coin {} = {}".format(coinCount, thisCoin))
        coinCount += 1
        coin = coin - thisCoin


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    print("Number of coins required for {} = {} coins".format(amnt, dpMakeChange(clist, amnt, coinCount, coinsUsed)))
    printCoins(coinsUsed, amnt)
    print("The list used = {}".format(coinsUsed))


main()

