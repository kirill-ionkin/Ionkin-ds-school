class Solution:
    def isValid(self, s: str) -> bool:
        same_brackets = {")": "(", "]": "[", "}": "{"}
        open_brackets = ("(", "[", "{")
        stack = list()

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                try:
                    open_bracket = stack.pop()
                    if open_bracket != same_brackets[bracket]:
                        return False
                except IndexError:
                    return False

        return False if len(stack) else True
