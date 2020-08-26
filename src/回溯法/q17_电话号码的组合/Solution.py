class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrace(index):
            if index==len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for each in phoneMap[digit]:
                    combination.append(each)
                    backtrace(index+1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrace(0)
        return combinations
