class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        Mul_lr = [0]*len(nums)
        Mul_rl = [0]*len(nums)

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            Mul_lr[i] = prod


        prod = 1
        for i in range(len(nums) - 1,-1,-1):
            prod *= nums[i]
            Mul_rl[i] = prod

        print("Mul_lr:", Mul_lr)
        print("Mul_rl:", Mul_rl)

        Mul_final = [0]*len(nums)

        Mul_final[0] = Mul_rl[1]
        Mul_final[len(nums) - 1] = Mul_lr[len(nums) - 2]
        print("Mul_final:", Mul_final)


        for i in range(1, len(nums)-1):
            Mul_final[i] = Mul_lr[i-1] * Mul_rl[i+1]

        return Mul_final