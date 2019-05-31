
def power(num, exp):
    if exp < 0:
        return power(1/num, abs(exp))

    if exp == 0: return 1
    return num * power(num, exp -1)



print(power(3, 3))
print(power(3, 0))
print(power(3, -3))
