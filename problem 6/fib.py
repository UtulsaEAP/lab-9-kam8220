def fibonacci(n):
  start_num=n

  
  if start_num<0:
    return -1
  if n==0:
   return 0
  elif n==1:
   return 1
  else:
  #write your code here
   return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')