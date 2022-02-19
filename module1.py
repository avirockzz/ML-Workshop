def EvenorOdd(n):
    if n%2==0:
        return 'Even'
    else:
        return 'odd'
    
def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    
def Table(n):
    for i in range(1,10+1):
        print(n,'*',i,'=',n*i)
        
def vowel_count(s):
    c=0
    for ch in s:
        if ch in 'aeiouAEIOU':
            c+=1
    print('Vowels_count:',c)