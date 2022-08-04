import random

be_list = [random.randint(0, 500) for i in range(100)]

print(be_list)
print(len(be_list))

left = min(be_list)
right = max(be_list)

print('left', left)
print('right', right)

search_num = int(input('enter num '))

while left < right - 1:
    mid = (left + right) // 2
    if mid > search_num:
        right = mid
    else:
        left = mid

if left >= 0 and left == search_num:
    print('true', be_list.index(left))
else:
    print('false')
