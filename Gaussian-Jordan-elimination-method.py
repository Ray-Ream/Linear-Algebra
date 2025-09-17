def gauss_jordan(proc_matrix):
    A = proc_matrix.copy()
    m = len(A)  # 列數
    n = len(A[0])  # 行數

    pivot_row = 0  # 處理錨點 (列)
    pivot_col = 0  # 處理錨點 (行)

    """先搜尋第一個非零元素的列並與第一行交換"""
    while pivot_col < n:
        # 尋找第一個非零元素的列
        for i in range(pivot_row, m):
            if abs(int(A[i][pivot_col])) > 0:  # 非零判斷閾值
                # 找到後與第一行交換
                if i != pivot_row:
                    A[pivot_row], A[i] = A[i], A[pivot_row]
                break
        else:
            # 如果該列全為零，跳到下一列
            pivot_col += 1
            continue
        break

    """高斯喬登消去法"""
    while pivot_row < m and pivot_col < n:
        # 如果當前主元為 0，跳到下一列
        if abs(int(A[pivot_row][pivot_col])) == 0:
            pivot_col += 1
            continue

        # 化為前導 1
        pivot = A[pivot_row][pivot_col]
        for j in range(n):
            A[pivot_row][j] = A[pivot_row][j] / pivot

        # 消去主元列的其他元素
        for i in range(m):  # 遍歷所有行
            if i != pivot_row:  # 不為當前所在的行
                factor = A[i][pivot_col]  # 獲取要消去的數值
                for j in range(n):
                    A[i][j] = A[i][j] - factor * A[pivot_row][j]

        pivot_row += 1
        pivot_col += 1

    return A


def print_matrix(proc_matrix):
    for row in proc_matrix:
        formatted_row = []
        for x in row:
            if abs(x) == 0:
                formatted_row.append(0)
            else:
                formatted_row.append(round(x, 2))
        print(formatted_row)


# 鍵盤輸入矩陣
def input_matrix_from_keyboard():
    print("請輸入矩陣的行數 (m) 和列數 (n)，以空格分隔：")
    m, n = map(int, input().split())
    matrix = []
    print(f"請輸入 {m} 行，每行 {n} 個數字，以空格分隔：")
    for i in range(m):
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
        # 檢查矩陣是否為有效矩陣（每行長度相同）
        if not res_matrix or not all(len(row) == len(res_matrix[0]) for row in res_matrix):
            raise ValueError("檔案中的矩陣格式無效，每行長度必須相同")
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
            [0, 0, 0, 1],
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3]
        ]
    elif choice == '3':
        filename = input("請輸入檔案名稱（例如 'matrix.txt'）：")
        matrix = input_matrix_from_file(filename)
        if matrix is None:
            exit(1)
    else:
        print("無效選擇，使用預設陣列輸入")
        matrix = [
            [0, 0, 0, 1],
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3]
        ]

    print("\n原始矩陣：")
    print_matrix(matrix)

    result = gauss_jordan(matrix)
    print("\n簡化列梯形 (RREF)：")
    print_matrix(result)
