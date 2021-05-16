def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of
square = nth_power(2)
#查看 __closure__ 的值
print(square.__closure__)