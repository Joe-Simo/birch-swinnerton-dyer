"""Validated rectangular interval integration; elementary tails proved in CHECKPOINT.md."""
from __future__ import annotations
from mpmath import iv
from math import ceil
from time import perf_counter
import json
from pathlib import Path
from coefficients import coefficients
iv.dps=25

def endpoints(x):
    return str(x.a),str(x.b)

def enclose(p:int, subdivisions:int=32):
    start=perf_counter()
    alpha=2*iv.pi/(iv.sqrt(32)*p)
    bound=16*p
    aa=coefficients(p,bound)
    total=iv.mpf(0);fourier_error=iv.mpf(0)
    slabs=[]
    A=1
    while A<128*p:
        B=2*A;K=max(1,ceil(bound/A));h=iv.mpf(A)/subdivisions
        val=iv.mpf(0)
        for j in range(subdivisions):
            lo=iv.mpf(A)+j*h;hi=iv.mpf(A)+(j+1)*h
            t=iv.mpf([lo.a,hi.b]);q=iv.exp(-alpha*t)
            ff=iv.mpf(aa[K])
            for a in reversed(aa[:K]):ff=ff*q+a
            val+=2*h*iv.log(t)**2*ff
        tail=4*iv.log(B)**2/alpha*iv.exp(-alpha*A*(K+1))/(1-iv.exp(-alpha*A))
        fourier_error+=tail
        total+=val
        slabs.append({'A':A,'B':B,'K':K,'interval':endpoints(val),'fourier_error_upper':str(tail.b)})
        A=B
    T=A
    tail=4*iv.exp(-alpha*T)/(1-iv.exp(-alpha*T))*(T*T/alpha+2*T/alpha**2+2/alpha**3)
    error=(fourier_error+tail).b
    result=total+iv.mpf([-error,error]);L2=alpha*result
    return {'p':p,'subdivisions':subdivisions,'coefficient_bound':bound,'T':T,'Lambda2_interval':endpoints(result),'L2_interval':endpoints(L2),'positive':bool(result.a>0),'slabs':slabs,'fourier_error_upper':str(fourier_error.b),'integration_tail_upper':str(tail.b),'seconds':perf_counter()-start}

if __name__=='__main__':
    import sys
    p=int(sys.argv[1]) if len(sys.argv)>1 else 41
    steps=int(sys.argv[2]) if len(sys.argv)>2 else 32
    result=enclose(p,steps)
    Path(__file__).with_name('results').joinpath(f'interval-{p}-{steps}.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k!='slabs'})
