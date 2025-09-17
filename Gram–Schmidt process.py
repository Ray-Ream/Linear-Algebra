def dot(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def scalar_mult(scalar, vec):
    return [scalar * x for x in vec]


def vec_subtract(v1, v2):
    return [x - y for x, y in zip(v1, v2)]


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


def gram_schmidt(matrix):
    """
    使用 Gram-Schmidt 過程將矩陣轉換為正交基
    v: 原始數值
    q: 映射後的正交
    """

    # 依序拿出matrix的行向量
    matrix = transpose(matrix)  # 轉置矩陣，將行向量轉為列向量

    orthogonal = []  # 正交
    for i in range(len(matrix)):
        vi = matrix[i]
        for j in range(i):  # 將之前的正交向量投影到當前向量上
            qj = orthogonal[j]
            proj_scale = dot(vi, qj) / dot(qj, qj) if dot(qj, qj) != 0 else 0  # 投影比例
            proj = scalar_mult(proj_scale, qj)  # 投影
            vi = vec_subtract(vi, proj)  # 減去投影
        orthogonal.append(vi)
    return orthogonal


def print_matrix(matrix, transpose_flag=False):
    if transpose_flag:
        matrix = transpose(matrix)  # 轉置回行向量形式
    for row in matrix:
        print([round(x, 4) if abs(x) >= 1e-10 else 0 for x in row])


# 以下維持輸入方式（鍵盤 / 檔案 / 預設）
def input_matrix_from_keyboard():
    print("請輸入行數 m（行向量數量）：")
    m = int(input())
    print("請輸入列數 n（每個向量的維度，n > m）：")
    n = int(input())
    if n <= m:
        raise ValueError("n 必須大於 m")

    matrix = []
    print(f"請輸入 {m} 行，每行 {n} 個浮點數，以空白分隔：")
    for i in range(m):
        row = list(map(float, input(f"第 {i + 1} 行：").split()))
        if len(row) != n:
            raise ValueError(f"第 {i + 1} 行應該輸入 {n} 個元素")
        matrix.append(row)
    return matrix


def input_matrix_from_file(proc_filename):
    res_matrix = []
    try:
        with open(proc_filename, 'r') as f:
            for line in f:
                row = [float(x) for x in line.strip().split()]
                res_matrix.append(row)
        n = len(res_matrix)
        if not all(len(row) == n for row in res_matrix):
            raise ValueError("檔案中的矩陣不是方陣")
        return res_matrix
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{proc_filename}'")
        return None
    except ValueError as e:
        print(f"錯誤：{e}")
        return None


# 主程式
if __name__ == "__main__":
    print("選擇輸入方式：")
    print("1. 鍵盤輸入")
    print("2. 預設矩陣")
    print("3. 檔案輸入")
    choice = input("請輸入選擇 (1/2/3)：")

    if choice == '1':
        matrix = input_matrix_from_keyboard()
    elif choice == '2':
        # 預設：3 個行向量，每個向量為 5 維
        matrix = [
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0]
        ]
    elif choice == '3':
        filename = input("請輸入檔名：")
        matrix = input_matrix_from_file(filename)
        if matrix is None:
            exit(1)
    else:
        print("無效選擇，使用預設矩陣")
        matrix = [
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0]
        ]

    print("\n原始矩陣：")
    print_matrix(matrix)

    orthogonal = gram_schmidt(matrix)
    print("\n正交化後矩陣：")
    print_matrix(orthogonal, transpose_flag=True)
