N = int(input())
nums = input().split(" ")
ints = [int(i) for i in nums]
mx = max(ints)
mn = min(ints)
print(mx-mn)
