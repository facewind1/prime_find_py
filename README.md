# Prime Find 🔢

一个基于 **6k ± 1 法则** 的高效质数（素数）判断程序。

## 算法原理

所有大于 3 的质数都分布在 6 的倍数的两侧，即可以表示为 $6k \pm 1$ 的形式。因此我们只需检查这些形式的数是否为因子，相比从 2 逐个试除，效率提升约 **3 倍**。

**推导过程**：
- 任意整数 $n \ge 5$ 可表示为 $6k, 6k\pm1, 6k\pm2, 6k+3$ 之一
- $6k$ 被 2,3 整除，$6k\pm2$ 被 2 整除，$6k+3$ 被 3 整除
- 因此只需检查 $6k \pm 1$ 形式的数

详见：[质数临近6的倍数附近 - CSDN](https://blog.csdn.net/huangzhaokun/article/details/107768609)

## 使用方法

### 前置要求

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/)（推荐的包管理器）

### 运行

```bash
# 使用 uv 运行
uv run main.py

# 或使用标准 Python
python main.py
```

### 示例

```
请输入一个整数: 9973
9973 是质数（素数）

请输入一个整数: 100
100 不是质数（素数）
```

## 项目结构

```
prime_find_py/
├── main.py          # 主程序
├── pyproject.toml   # 项目配置
└── README.md        # 本文件
```

## 许可

MIT License
