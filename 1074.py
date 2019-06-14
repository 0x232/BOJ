def visit(N, r, c):
    if N == 1:
        return 2*r + c
    L, idx = 2**N, (2**(2*(N-1)))
    if r < L//2 and c < L//2:
        return visit(N-1, r, c)
    if r < L//2 and c >= L//2:
        return idx + visit(N-1, r, c % (L//2))
    if r >= L//2 and c < L//2:
        return idx*2 + visit(N-1, r % (L//2), c)
    if r >= L//2 and c >= L//2:
        return idx*3 + visit(N-1, r % (L//2), c % (L//2))

N, r, c = map(int, input().split())
print(visit(N, r, c))
