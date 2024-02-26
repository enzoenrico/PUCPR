n = int(input('[+]Insira um numero para a conversao: \n'))

nums = []

while( n > 0):
    nums.append(int(n % 2))
    n = int(n / 2)
nums = nums[::-1]
nums = ' '.join(str(e) for e in nums)
print(nums)
