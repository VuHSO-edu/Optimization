

import gurobipy as gp
from gurobipy import GRB

# BAI TAP 05

# Đặt biến theo phương thức nhị phân:
    # Đặt X[i,j] = 1 khi đối tượng i được tô màu j và X[i,j] = 0 khi đối tượng i không được tô màu j
# Các ràng buộc:
    # Mỗi đối tượng i chỉ được tô 1 màu
        # Điều kiện: Σj=1->k X[i,j] = 1
    # Hai đối tượng liền kề không được tô cùng màu
        # Điều kiện: Σi=1->(n-1) Σj=1->k X[i,j] + X[i+1,j] <= 1
# Hàm mục tiêu: Chúng ta cần tìm là lời giải thỏa mãn các ràng buộc nên hàm mục tiêu không cần thiết và có thể đặt hàm mục tiêu là 0


# Hàm solve coloring problem
def solve_coloring_problem(n,k):
    model = gp.Model("Coloring problem")

    # Tạo biến X[i,j] nhị phân
    x = model.addVars(n, k, vtype = GRB.BINARY, name = "x")

    # Ràng buộc 1 : Mỗi đối tượng i chỉ được tô 1 màu
    for i in range(n):
        model.addConstr(sum(x[i,j] for j in range(k)) == 1, name = f"constraint1_{i}")

    # Ràng buộc 2 : Hai đối tượng liền kề không được tô cùng màu
    for i in range(n-1):
        for j in range(k):
            model.addConstr(x[i,j] + x[i+1,j] <= 1, name = f"constraint2_{i}_{j}")

    # Hàm mục tiêu
    model.setObjective(0, GRB.MINIMIZE)

    # Tối ưu hóa mô hình
    model.optimize()

    # In kết quả
    if model.status == GRB.OPTIMAL:
        solution = {}
        for i in range(n):
            for j in range(k):
                if x[i,j].x == 1:
                    solution[i] = j
        print("Kết quả tô màu:")
        for i in range(n):
            print(f"Đối tượng {i} tô màu {solution[i]}")
    else:
        print("Không tìm được lời giải")


# Giải bài toán với n = 8, k = 2
solve_coloring_problem(8,2)


# --------------------------------------------------------------------------------------------------



# BAI TAP 06
# Trên bàn cờ 8x8 có 64 ô vuông
# Đặt biến theo phương pháp nhị phân:
    # x[i, j] = 1 khi có quân hậu
    # x[i, j] = 0 khi không có quân hậu
# Các ràng buộc:
    # Ràng buộc 1: Mỗi hàng chỉ có 1 quân hậu
        # Điều kiện: Σj=1->8 x[i,j] <= 1
    # Ràng buộc 2: Mỗi cột chỉ có 1 quân hậu
        # Điều kiện: Σi=1->8 x[i,j] <= 1
    # Ràng buộc 3: Mỗi đường chéo chính chỉ có 1 quân hậu
        # Có 15 đường chép chính. Biểu diễn đường chéo chính bằng cách i-j = k suy ra k chạy từ -7 đến 7
        # Điều kiện: Σk=-7->7 x[i,j] <= 1
    # Ràng buộc 4: Mỗi đường chéo phụ chỉ có 1 quân hậu
        # Có 15 đường chép phụ. Biểu diễn đường chéo phụ bằng cách i+j = k suy ra k chạy từ 2 đến 16
        # Điều kiện: Σk=2->16 x[i,j] <= 1
# Hàm mục tiêu: Chúng ta cần tìm là số quân hậu nhiều nhất có thể đặt trên bàn cờ nên hàm mục tiêu sẽ là tổng số quân hậu
    # Max Σi=1->8 Σj=1->8 x[i,j]

def solve_N_queens_problem(n):
    model = gp.Model("N-Queens problem")

    # Tạo biến x[i,j] nhị phân
    x = model.addVars(n, n, vtype = GRB.BINARY, name = "x")

    # Ràng buộc 1: Mỗi hàng chỉ có 1 quân hậu
    for i in range(n):
        model.addConstr(sum(x[i,j] for j in range(n)) <= 1, name = f"constraint1_{i}")

    # Ràng buộc 2: Mỗi cột chỉ có 1 quân hậu
    for j in range(n):
        model.addConstr(sum(x[i,j] for i in range(n)) <= 1, name = f"constraint2_{j}")

    # Ràng buộc 3: Mỗi đường chéo chính chỉ có 1 quân hậu
    for k in range(-n+1,n):
        model.addConstr(sum(x[i,i-k] for i in range(n) if 0 <= i-k < n) <= 1, name = f"constraint3_{k}")

    # Ràng buộc 4: Mỗi đường chéo phụ chỉ có 1 quân hậu
    for k in range(2,2*n):
        model.addConstr(sum(x[i,k-i] for i in range(n) if 0 <= k-i < n) <= 1, name = f"constraint4_{k}")

    # Hàm mục tiêu
    model.setObjective(sum(x[i,j] for i in range(n) for j in range(n)), GRB.MAXIMIZE)

    # Tối ưu hóa mô hình
    model.optimize()

    # In kết quả
    if model.status == GRB.OPTIMAL:
        print("Kết quả đặt quân hậu:")
        for i in range(n):
            for j in range(n):
                if x[i,j].x == 1:
                    print(f"Quân hậu tại hàng {i}, cột {j}")
    else:
        print("Không tìm được lời giải")


# Giải bài toán với n = 8
solve_N_queens_problem(8)
