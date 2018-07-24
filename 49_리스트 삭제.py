nums = [1, 2, 3, 4, 5]
del nums[4]  # 인덱스로 접근하여 삭제
print(nums)
del nums[3:4] #슬라이싱 삭제 가능.
print(nums)
nums.remove(2)  # 요소로 접근하여 삭제
print(nums)

