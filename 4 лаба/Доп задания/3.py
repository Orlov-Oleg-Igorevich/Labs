def Karacuba(a, b):
    if len(str(a)) % 2 != 0 or len(str(b)) % 2 != 0 or len(str(a)) != len(str(b)):
        return 'Не сработает'
    T = int('9'*(len(str(a))//2)) + 1
    a_lst = [a//T, a-T*(a//T)]
    b_lst = [b//T, b-T*(b//T)]
    return T**2 * a_lst[0] * b_lst[0] + T*((a_lst[0] + a_lst[1])*(b_lst[0] + b_lst[1]) - a_lst[0]*b_lst[0] - a_lst[1]*b_lst[1]) + a_lst[1]*b_lst[1]

print(Karacuba(4167842617842176424412414124412412, 4167842617842176424412414124412412))