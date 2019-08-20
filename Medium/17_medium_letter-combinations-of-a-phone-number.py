class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combi = {"2": "abc", "3": "def",
                "4": "ghi", "5": "jkl", "6": "mno",
                "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = [""]
        for digit in digits:
            ans = self.combine(ans, combi[digit])
        return ans
    
    def combine(self, ans: List[str], letters: str) -> List[str]:
        new_ans = []
        for letter in letters:
            for string in ans:
                new_string = string + letter
                new_ans.append(new_string)
        return new_ans
        
        
        
