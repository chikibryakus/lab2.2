for num in range(100, 1000):
 if num % 7 == 0 and sum(int(digit) for digit in str(num)) % 7 == 0:
  print(num)
