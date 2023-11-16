import math
import struct


class FileWorkAndCalc:
    def __init__(self):
        self.result = 0.0

    def write_res_txt(self, file_name):
        # Writing result to a text file
        with open(file_name, 'w') as file:
            file.write(f'{self.result} ')

    def read_res_txt(self, file_name):
        try:
            # Reading result from a text file
            with open(file_name, 'r') as file:
                self.result = float(file.read())
        except FileNotFoundError as ex:
            print(ex)

    def write_res_bin(self, file_name):
        try:
            # Writing result to a binary file
            with open(file_name, 'wb') as file:
                file.write(struct.pack('d', self.result))
        except (FileNotFoundError, IOError) as ex:
            print(ex)

    def read_res_bin(self, file_name):
        try:
            # Reading result from a binary file
            with open(file_name, 'rb') as file:
                packed_data = file.read(8)  # Assuming a double is 8 bytes
                self.result = struct.unpack('d', packed_data)[0]
        except (FileNotFoundError, IOError) as ex:
            print(ex)

    def calculate(self, x):
        try:
            rad = x * math.pi / 180.0
            y = 1 / math.tan(2 * rad)
            y = math.sin(3 * rad - 5) / y

            if math.isnan(y) or math.isinf(y) or x == 0 or x == 90:
                raise ArithmeticError

        except ArithmeticError:
            if rad == math.pi / 2.0 or rad == 0.0:
                raise CalcException("Exception reason: Illegal value of X for cotangent calculation")
            elif math.tan(2 * rad) == 0 or 1 / math.tan(2 * rad) == 0:
                raise CalcException("Exception reason: Division by 0")
            else:
                raise CalcException("Unknown reason of the exception during exception calculation")

        self.result = y

    def get_result(self):
        return self.result


class CalcException(ArithmeticError):
    def __init__(self, cause=None):
        super().__init__(cause)


def main():
    obj = FileWorkAndCalc()
    print("Enter x: ", end='')

    try:
        data = input()
        obj.calculate(float(data))
        print("Result is:", obj.get_result())

        obj.write_res_txt("test1.txt")
        obj.write_res_bin("test2.bin")

        obj.read_res_bin("test2.bin")
        print("Result from binary file is:", obj.get_result())

        obj.read_res_txt("test1.txt")
        print("Result from test file is:", obj.get_result())

    except (ValueError, CalcException) as ex:
        print(ex)


if __name__ == "__main__":
    main()


