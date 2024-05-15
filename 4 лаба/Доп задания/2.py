import struct

def Q_rsqrt(number):
    x2 = number * 0.5
    threehalfs = 1.5

    conv = struct.unpack('I', struct.pack('f', number))[0]
    conv = 0x5f3759df - (conv >> 1)
    conv = struct.unpack('f', struct.pack('I', conv))[0]
    conv *= threehalfs - x2 * conv * conv

    return conv

print("Приблизительная ошибка: ")
print(Q_rsqrt(25) - (1/57.09**0.5))