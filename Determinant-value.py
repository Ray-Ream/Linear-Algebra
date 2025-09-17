def determinant(matrix):
    # 檢查是否為方陣
    n = len(matrix)
    if n != len(matrix[0]):
        print("行列式不存在！（不是方陣）")
        return None

    A = [row[:] for row in matrix]  # 複製避免破壞原始資料
    sign = 1  # 記錄列交換的正負號

    for i in range(n):
        # 找尋主對角元素（pivot）
        if abs(A[i][i]) < 1e-10:
            found = False
            for k in range(i + 1, n):
                if abs(A[k][i]) > 1e-10:
                    A[i], A[k] = A[k], A[i]
                    sign *= -1
                    found = True
                    break
            if not found:
                return 0  # 有整列為0 → 行列式為0

        # 將下方元素消成 0（形成上三角）
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # 行列式 = 主對角線乘積 × sign
    det = sign
    for i in range(n):
        det *= A[i][i]
    return det


def print_matrix(proc_matrix):
    for row in proc_matrix:
        formatted_row = []
        for x in row:
            if abs(x) < 1e-10:
                formatted_row.append(0)
            else:
                formatted_row.append(round(x, 2))
        print(formatted_row)


# 以下維持輸入方式（鍵盤 / 檔案 / 預設）
def input_matrix_from_keyboard():
    print("請輸入矩陣的行數 (n)：")
    n = int(input())
    matrix = []
    print(f"請輸入 {n} 行，每行 {n} 個數字，以空格分隔：")
    for i in range(n):
        row = list(map(float, input(f"第 {i + 1} 行：").split()))
        if len(row) != n:
            raise ValueError(f"第 {i + 1} 行應有 {n} 個元素，但輸入 {len(row)} 個")
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
    print("2. 陣列輸入（預設矩陣）")
    print("3. 檔案輸入")
    choice = input("請輸入選擇 (1/2/3)：")

    if choice == '1':
        matrix = input_matrix_from_keyboard()
    elif choice == '2':
        matrix = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]
        ]
    elif choice == '3':
        filename = input("請輸入檔案名稱（例如 'matrix.txt'）：")
        matrix = input_matrix_from_file(filename)
        if matrix is None:
            exit(1)
    else:
        print("無效選擇，使用預設陣列輸入")
        matrix = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]
        ]

    print("\n原始矩陣：")
    print_matrix(matrix)

    det = determinant(matrix)
    if det is not None:
        print(f"\n行列式的值：{round(det, 4)}")
