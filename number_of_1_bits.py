

def hammingweight(n):
    count = 0

    n = list(map(int, str(bin(n)[2:])))

    for i in n:
        if i == 1:
            count = count + 1
    print(count)


def main():

    hammingweight(int('00000000000000000000000000001011', 2))
    hammingweight(int('00000000000000000000000010000000', 2))
    hammingweight(int('11111111111111111111111111111101', 2))


if __name__ == "__main__":
    main()
