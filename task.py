#Question 1: Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.
print("Question 1: ")
def question1():
    s = input("Enter a string: ")
    list = s.split()
    last_word = list[-1]
    print(len(last_word))

question1()

#Question 2: Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 0 <= a, b, c, d < n a, b, c, and d are distinct. nums[a] + nums[b] + nums[c] + nums[d] == target You may return the answer in any order.
print("Question 2: ")
def question2(nums, target):
    nums = [int(num) for num in nums]
    quadruplets = []
    n = len(nums)

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplet = [nums[a], nums[b], nums[c], nums[d]]
                        quadruplet.sort()
                        if quadruplet not in quadruplets:
                            quadruplets.append(quadruplet)

    return quadruplets
nums = input("Enter a list of numbers: ").split()
target = int(input("Enter a target number: "))
result = question2(nums, target)
print(result)