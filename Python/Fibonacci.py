
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
def fib_mod(n, m):
    if n <= 1:
        return n

    prev, cur = 0, 1

    for i in range (1, n):
        prev, cur = cur % m, (prev + cur) % m

    return cur


def main():
    # n = int(input())
    # print(fib(n))
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
