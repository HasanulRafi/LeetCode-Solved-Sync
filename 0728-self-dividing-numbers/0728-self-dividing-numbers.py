class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for number in range(left, right + 1):
            string = str(number)
            if "0" in string:
                continue
            answer.append(number)
            for i in string:
                if number % int(i) != 0:
                    answer.pop()
                    break
        return answer 