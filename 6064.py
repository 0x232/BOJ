import math
for _ in range(int(input())):
    M, N, x, y = map(int, input().split())

    if M == N:
        print(x)
    else:
        z = (M+x-y)%M if M<N else (N+y-x)%N
        O = N%M if M<N else M%N
        if z%math.gcd(M,N)!=0:
            print(-1)
        else:
            Z = ((z+(O-1)*N)%O)*N+z if M<N else ((z+(O-1)*M)%O)*M+z
            print(N*Z//O+y if M<N else M*Z
                  //O+x)
