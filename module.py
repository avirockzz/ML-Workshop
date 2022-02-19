def factors(n):
    for i in range(1,n+1):  #(1,n//2+1)
        if n%i==0:
            print(i,end=" ")

def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    #print('sum:',s)
    if s==n:
        return True
    else:
        return False
    
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False