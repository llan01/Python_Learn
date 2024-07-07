def fac(n): #n的阶乘 N！=N*（N-）！...1!=1
       if n==1:
              return 1
       else:
              return n*fac(n-1)
print(fac(5))