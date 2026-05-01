import math


def is_prime(n: int) -> bool:
    """
    判断一个数是否为质数（素数）。

    使用 "质数临近 6 的倍数" 算法（6k ± 1 法则）：
    所有大于 3 的质数都可以表示为 6k ± 1 的形式，
    因此只需检查这些形式的数是否为因子。
    """
    # 1 和小于 1 的数不是质数
    if n <= 1:
        return False
    # 2 和 3 是质数
    if n <= 3:
        return True
    # 排除能被 2 或 3 整除的数
    if n % 2 == 0 or n % 3 == 0:
        return False

    # 从 5 开始，检查 6k ± 1 形式的数
    # 即 i = 5, 7, 11, 13, 17, 19, ...
    limit = int(math.isqrt(n))
    i = 5
    while i <= limit:
        # 先检查 6k-1（即当前的 i），再检查 6k+1（即 i+2）
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # 步长为 6，跳到下一组 6k±1

    return True


def main():
    """主函数：读取用户输入并判断是否为质数。"""
    try:
        num = int(input("请输入一个整数: "))
    except ValueError:
        print("输入无效，请输入一个整数。")
        return

    if is_prime(num):
        print(f"{num} 是质数（素数）")
    else:
        print(f"{num} 不是质数（素数）")


if __name__ == "__main__":
    main()
