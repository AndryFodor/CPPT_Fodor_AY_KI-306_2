def main():
    SIZE = 0
    iter = 0
    ok = False

    symbol = input("Enter symbol for filling the matrix: ")
    if len(symbol) == 1:
        print("Now enter the size of matrix")
        SIZE = int(input())
        arr = [[' ' for _ in range(SIZE - i)] for i in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                if i <= j:
                    arr[i][j - i] = symbol

        # Printing of matrix
        with open("MyFile.txt", "w") as fout:
            for i in range(SIZE):
                for j in range(SIZE):
                    if i < SIZE / 2:
                        if i <= j:
                            print(arr[i][j - i], end=" ")
                            fout.write(arr[i][j - i] + " ")
                        else:
                            print(" ", end=" ")
                            fout.write("  ")
                    else:
                        if i <= j:
                            if not ok:
                                for k in range(iter):
                                    print(" ", end=" ")
                                    # fout.write(" ")
                                ok = True
                            print(arr[i][j - i], end=" ")
                            # fout.write(arr[i][j - i] + " ")

                print()
                fout.write("\n")
                if i >= SIZE / 2:
                    iter += 1
                    ok = False

            fout.flush()

    elif len(symbol) == 0:
        print("You forgot to enter the symbol")
    else:
        print("You entered more than one symbol")


if __name__ == "__main__":
    main()
