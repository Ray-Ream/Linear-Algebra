def gauss_jordan_inverse(proc_matrix):
    # 檢查是否為方陣
    n = len(proc_matrix)
    if n != len(proc_matrix[0]):
        print("反矩陣不存在！（不是方陣）")
        return None

    # 創建增廣矩陣 [A | I]
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(proc_matrix)]

    pivot_row = 0  # 主元列
    pivot_col = 0  # 主元行

    # 高斯-喬登消去法
    while pivot_row < n and pivot_col < n:
        # 尋找主元，若當前主元為 0，則嘗試交換
        if abs(A[pivot_row][pivot_col]) < 1e-10:
            found_non_zero = False
            for i in range(pivot_row + 1, n):
                if abs(A[i][pivot_col]) > 1e-10:
                    A[pivot_row], A[i] = A[i], A[pivot_row]
                    found_non_zero = True
                    break
            if not found_non_zero:
                print("反矩陣不存在！（矩陣不可逆）")
                return None

        # 將主元化為 1
        pivot = A[pivot_row][pivot_col]
        for j in range(2 * n):
            A[pivot_row][j] /= pivot

        # 消去主元列的其他行
        for i in range(n):
            if i != pivot_row:
                factor = A[i][pivot_col]
                for j in range(2 * n):
                    A[i][j] -= factor * A[pivot_row][j]

        pivot_row += 1
        pivot_col += 1

    # 提取反矩陣
    inverse = [row[n:] for row in A]
    return inverse


def print_matrix(proc_matrix):
    for row in proc_matrix:
        formatted_row = []
        for x in row:
            if abs(x) < 1e-10:  # 將極小值視為 0
                formatted_row.append(0)
            else:
                formatted_row.append(round(x, 2))  # 保留兩位小數
        print(formatted_row)


# 鍵盤輸入矩陣
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


# 從檔案輸入矩陣
def input_matrix_from_file(proc_filename):
    res_matrix = []
    try:
        with open(proc_filename, 'r') as f:
            for line in f:
                row = [float(x) for x in line.strip().split()]
                res_matrix.append(row)
        # 檢查是否為方陣
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
        ]  # 預設 3x3 可逆矩陣
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

    inverse = gauss_jordan_inverse(matrix)
    if inverse:
        print("\n反矩陣：")
        print_matrix(inverse)