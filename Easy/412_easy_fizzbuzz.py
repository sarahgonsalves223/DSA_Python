class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        soln = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                soln.append("FizzBuzz")
            elif i%3 == 0:
                soln.append("Fizz")
            elif i%5 == 0:
                soln.append("Buzz")
            else:
                soln.append(str(i))
        return soln