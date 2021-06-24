def sum13(nums):
    sums = 0
    if len(nums) > -1:
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 13:
                i +=2
            else:
                sums += nums[i]
                i +=1
        return sums
    else:
        return  0
print(sum13([1, 2, 13, 2, 1, 13]))
