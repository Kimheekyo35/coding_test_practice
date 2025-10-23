n = int(input())

# Please write your code here.

def func_return(n):
    if n == 0:
        return
    print('HelloWorld')
    func_return(n-1)
    

func_return(n)
