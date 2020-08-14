import math


# Дано целое число 1≤n≤40 1 \le n \le 40 1≤n≤40, необходимо вычислить n n n-е число Фибоначчи (напомним, что F0=0 F_0=0 F0​=0, F1=1 F_1=1 F1​=1 и Fn=Fn−1+Fn−2 F_n=F_{n-1}+F_{n-2} Fn​=Fn−1​+Fn−2​ при n≥2 n \ge 2 n≥2).
def fib(n):
    if n <= 1:
        return n

    fibs = [0, 1]

    for i in range(2, n + 1):
      fibs.append(fibs[i - 2] + fibs[i - 1])

    return fibs[n]


# Дано число 1≤n≤107 1 \le n \le 10^7 1≤n≤107, необходимо найти последнюю цифру n n n-го числа Фибоначчи.
def fib_digit(n):
    if n <= 1:
        return n

    prev, cur = 0, 1

    for i in range (1, n):
        prev, cur = cur % 10, (prev + cur) % 10

    return cur


# Даны целые числа 1≤n≤1018 1 \le n \le 10^{18} 1≤n≤1018 и 2≤m≤105 2 \le m \le 10^5 2≤m≤105, необходимо найти остаток от деления n n n-го числа Фибоначчи на m m m.
# Используем период Пезано для оптимизации вычисления
# https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%9F%D0%B8%D0%B7%D0%B0%D0%BD%D0%BE

def get_lines_count(m, line_last_item):
    degree = 1

    while (line_last_item ** degree % m != 1):
        degree += 1

    return degree


def get_period_line(n, m):
    period_line = [0, 1]
    prev, cur = 0, 1

    while (cur < n):
        prev, cur = cur, (prev + cur) % m

        if cur == 0:
            break

        period_line.append(cur)

    if cur >= n:
        return None, None
    else:
        return period_line, prev


def fib_mod(n, m):
    if n <= 1:
        return n

    period_line, last_item = get_period_line(n, m)
    if period_line == None:
        return n % m

    period_line_length = len(period_line)

    x = n % period_line_length
    y = math.floor(n / period_line_length)

    # print(period_line[x], '*', last_item, ' ** ', y, ' % ', m)
    return period_line[x] * pow(last_item, y, m) % m


def main():
    # n = int(input())
    # print(fib(n))
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
