#coding:utf-8
"""
面倒なことをしているがソート後は中央値を取ればよかった
"""

N = int(input())
nums = input().split(" ")
nums2 = [int(x)-i-1 for i,x in enumerate(nums)]
nums2.sort()
length = len(nums2)
numpre = 0
same = 1
if length == 1:
    value = nums2[0]

for n,m in zip(nums2[:-1],nums2[1:]):
    if n == m:
        same += 1
    else:
        impact = same + numpre
        if impact > length-impact:
            value = n
            break
        numpre += same
        same = 1
    value = m
    
answer = 0
for i in nums2:
    answer += abs(i-value)
print(answer)
