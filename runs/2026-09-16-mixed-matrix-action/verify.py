from collections import deque
import json

def mm(A,B,n):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%n for j in range(2)) for i in range(2))

def det(A,n):
    return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%n
I=((1,0),(0,1))

def closure(n):
    H=((1%n,(-2)%n),(0,1%n)); V=((1%n,0),((-2)%n,1%n))
    hi=((1%n,2%n),(0,1%n)); vi=((1%n,0),(2%n,1%n))
    gens=(H,V,hi,vi)
    seen={I if n>1 else ((0,0),(0,0))}
    q=deque(seen)
    while q:
        A=q.popleft()
        for g in gens:
            B=mm(g,A,n)
            if B not in seen:
                seen.add(B);q.append(B)
    assert all(det(A,n)==1%n for A in seen)
    return len(seen)

expected={2:1,3:24,4:4,5:120,7:336,8:32,13:2184,17:4896}
out={n:closure(n) for n in expected}
assert out==expected
for p in (3,5,7,13,17):
    assert out[p]==p*(p*p-1)
print(json.dumps({'status':'passed','image_sizes':out,'odd_prime_images':'full SL2 for tested primes'},indent=2))
