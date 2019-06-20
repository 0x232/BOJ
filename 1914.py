def number_of_movement(N):
    if N == 1:
        return 1
    else:
        return 2*number_of_movement(N-1) + 1


def print_movement(A, B, N):
    if N == 1:
        print(A, B)
    else:
        print_movement(A, 6-A-B, N-1)
        print(A, B)
        print_movement(6-A-B, B, N-1)

N = int(input())
print(number_of_movement(N))
if N <= 20:
    print_movement(1, 3, N)
