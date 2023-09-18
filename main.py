

def calc_roots(a, b, c):

    diskr = b ** 2 - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                return "Бесконечное число решений"
            else:
                return "Нет корней при a = 0, b = 0 при c != 0"
        else:
            root = -c / b
            return root
    elif diskr > 0:
        root1 = (-b + diskr ** 0.5) / (2 * a)
        root2 = (-b - diskr ** 0.5) / (2 * a)
        return root1, root2
    elif diskr == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        return "Нет корней"


def is_valid(co_str):

    if not co_str:
        return False

    # if co_str.startswith('+'):
    #     co_str = co_str[1:]
    #
    # if co_str.startswith('-'):
    #     co_str = co_str[1:]

    invalid_chars = set(co_str) - set("0123456789.+-")
    if invalid_chars:
        return False

    if co_str.startswith('.'):
        return False

    if co_str.count('.') > 1:
        return False

    if co_str.count("+") > 1:
        return False

    if co_str.count("-") > 1:
        return False

    coeff = float(co_str)
    return -1e15 <= coeff <= 1e15

# Можно допилить еще числа с "e"

# a_str = input("Введите число А - ").strip()
# b_str = input("Введите число B - ").strip()
# c_str = input("Введите число C - ").strip()


a_str = ''.join(input("Введите коэффициент a: ").strip().split(' '))
b_str = ''.join(input("Введите коэффициент b: ").strip().split(' '))
c_str = ''.join(input("Введите коэффициент c: ").strip().split(' '))

if is_valid(a_str) and is_valid(b_str) and is_valid(c_str):

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)

    if a == 0 and b == 0 and c == 0:
        print("Бесконечное число решений (0x^2 + 0x + 0 = 0)")
    else:

        roots = calc_roots(a, b, c)
        print("Корнями квадратного уравнения будут:")
        print(roots)

else:
    print("Введены некорректные коэффициенты. Попробуйте снова")
