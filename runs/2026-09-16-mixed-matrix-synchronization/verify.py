from collections import deque
import json

def mm(A,B,n): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%n for j in range(2)) for i in range(2))
def mpow(A,k,n):
    R=((1%n,0),(0,1%n))
    while k:
        if k&1:R=mm(R,A,n)
        A=mm(A,A,n);k//=2
    return R

def closure(n):
    H=((1%n,(-2)%n),(0,1%n));V=((1%n,0),((-2)%n,1%n));Hi=((1%n,2%n),(0,1%n));Vi=((1%n,0),(2%n,1%n))
    I=((1%n,0),(0,1%n));seen={I};q=deque([I])
    while q:
        A=q.popleft()
        for g in (H,V,Hi,Vi):
            B=mm(g,A,n)
            if B not in seen:seen.add(B);q.append(B)
    return len(seen)

def sl2_prime_size(p):return p*(p*p-1)
expected={15:sl2_prime_size(3)*sl2_prime_size(5),21:sl2_prime_size(3)*sl2_prime_size(7),35:sl2_prime_size(5)*sl2_prime_size(7),65:sl2_prime_size(5)*sl2_prime_size(13)}
out={n:closure(n) for n in expected}
assert out==expected
for n in (3,5,7,9,13,15):
    H=((1%n,(-2)%n),(0,1%n));V=((1%n,0),((-2)%n,1%n))
    for a in range(n):
        k=(-a*pow(2,-1,n))%n
        assert mpow(H,k,n)==((1%n,a),(0,1%n))
        assert mpow(V,k,n)==((1%n,0),(a,1%n))
print(json.dumps({'status':'passed','composite_image_sizes':out,'elementary_power_moduli':[3,5,7,9,13,15]},indent=2))
