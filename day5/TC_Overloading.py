class Calculator:
    def add(self, *nums):
        result = 0
        for i in nums:
            result+=i
        print(result)
cal=Calculator()
cal.add(1,2)
cal.add(1,2,3)
