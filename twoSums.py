#Question(Easy)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


# Function for the main logic of the code
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i != j and nums[i] + nums[j] == target):
                return [i, j]


# taking list as input
lst = []
n = int(input("Enter the number of element:"))
for i in range(n):
    elem = int(input("Enter the elements:"))
    lst.append(elem)

tar = int(input("Enter the targeted sum:"))
print("The output is:", twoSum(lst, tar))
