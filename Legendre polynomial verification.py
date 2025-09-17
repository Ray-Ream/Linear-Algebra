def dot(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def scalar_mult(s, v):
    return [s * x for x in v]


def vec_subtract(v1, v2):
    return [x - y for x, y in zip(v1, v2)]


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


def linspace(start, end, num):
    step = (end - start) / (num - 1)
    return [start + i * step for i in range(num)]


def gram_schmidt(matrix):
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


# 主程式
if __name__ == "__main__":
    print("輸入想要取樣的數值:")
    n = int(input().strip())

    # 1. 取樣點數
    x_values = linspace(-1, 1, n)
    print(f"取樣點數 (x_values)： {x_values}")

    # 2. 標準基底函數 → 向量形式
    f0 = [1 for x in x_values]  # 對應到 P0(x) = 1
    f1 = [x for x in x_values]  # 對應到 P1(x) = x
    f2 = [x ** 2 for x in x_values]  # 還沒正交，將正交後變為 P2
    print("各函數取樣點數結果：")
    print(f0)
    print(f1)
    print(f2)

    # 3. 將三個向量轉為一個 n × 3 的矩陣，每列是三個向量對應位置的值
    calc_matrix = [f0, f1, f2]
    calc_matrix = transpose(calc_matrix)  # 轉置矩陣，將行向量轉為列向量

    # 4. 執行 Gram-Schmidt 正交化
    orthogonal_vecs = gram_schmidt(calc_matrix)

    # 5. 輸出正交化向量
    print("正交化後三個向量：")
    print_matrix(orthogonal_vecs)

    # 5. 驗證正交性：Q0·Q1、Q0·Q2、Q1·Q2 應為 0
    print("\n驗證正交性（兩兩內積應近似為 0）：")
    for i in range(3):
        for j in range(i + 1, 3):
            d = dot(orthogonal_vecs[i], orthogonal_vecs[j])
            print(f"dot(Q{i}, Q{j}) = {d:.6f}")
