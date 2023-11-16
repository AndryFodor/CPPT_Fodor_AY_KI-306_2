def main():
    SIZE = 0
    symbol = ''
    data_file = open("MyFile.txt", "w")

    print("Enter symbol for filling the matrix")
    symbol = input()

    if len(symbol) == 1:
        print("Now enter the size of matrix")
        SIZE = int(input())
        arr = [[' ' for _ in range(SIZE - i)] for i in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                if i <= j:
                    arr[i][j - i] = symbol

        # Printing of matrix
        for i in range(SIZE):
            for j in range(SIZE):
                if i <= j:
                    print(arr[i][j - i], end=' ')
                    data_file.write(arr[i][j - i] + ' ')
                else:
                    print(' ', end=' ')
                    data_file.write('  ')
            print()
            data_file.write("\n")

        data_file.flush()
        data_file.close()

    elif len(symbol) == 0:
        print("You forgot to enter the symbol")
    else:
        print("You entered not a symbol")


if __name__ == "__main__":
    main()
