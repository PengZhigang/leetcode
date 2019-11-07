class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        res = []
        for i in range(len(nums)):
           for j in range(i+1, len(nums)):
               if (nums[i] + nums[j] == target):
                    res.append(i)
                    res.append(j)
                    break
        return res


def main():
    list = [2,7,11,15]
    print(Solution.twoSum(Solution, list, 9))

if __name__ == "__main__":
    # execute only if run as a script
    main()