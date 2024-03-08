def is_fibonacci(n):
  
  a, b = 0, 1
  for i in range(1, n + 1):
    c = a + b
    if c == n:
      return True
    a, b = b, c
  return False

number = int(input())
if is_fibonacci(number):
  print("True")
else:
  print("False")
