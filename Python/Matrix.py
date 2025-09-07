def read_matrix(name):
    print(f"Enter elements of Matrix {name} (3x3):")
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            val = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    C = [[0 for _ in range(3)] for _ in range(3)]  # fresh independent rows
    for i in range(3):
        for j in range(3):
            C[i][j] = A[i][j] + B[i][j]
    return C

def print_matrix(M, title="Matrix"):
    print(title)
    for row in M:
        print(row)

if __name__ == "__main__":
    A = read_matrix("A")
    B = read_matrix("B")

    print_matrix(A, "Matrix A:")
    print_matrix(B, "Matrix B:")

    C = add_matrices(A, B)
    print_matrix(C, "Result (A + B):")
