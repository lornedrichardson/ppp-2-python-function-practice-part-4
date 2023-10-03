def max_num(x, y, z):
  return max([x, y, z])

print(max_num(5, 2, 25))

def mult_list(list):
  if len(list) == 0:
    return 0
  else:
    product = list[0]
    for i in list[1:]:
      product = product * i
    return product

print(mult_list([5, 2, 25]))

def rev_string(string):
  return string[::-1]

print(rev_string("not a palindrome"))

def num_within(number, begin, end):
  return number in range(begin, end + 1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

triangle = [[1], [1, 1]]
def pascal(n):
  if n < 1:
    print("There must be at least 1 row.")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row_current = []
      row_previous = triangle[row_number - 1]
      row_length = len(row_previous) + 1
      for i in range(row_length):
        if i == 0:
          row_current.append(1)
        elif i > 0 and i < row_length - 1:
          row_current.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
        else:
          row_current.append(1)
      triangle.append(row_current)
      row_number += 1
    
    for row in triangle:
      print(row)

pascal(0)
pascal(1)
pascal(5)