import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        same_brackets = {")": "(", "]": "[", "}": "{"}
        open_brackets = ("(", "[", "{")
        stack = []

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

        return not len(stack)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("", True),
        ("[]", True),
        ("{}", True),
        ("()", True),
        ("{{{}}}", True),
        ("[([)]]", False),
        ("((())))", False),
        ("(({)})", False),
        ("[][][]{}{}{}()()()", True),
    ],
)
def test_isvalid(test_input, expected):
    assert Solution().isValid(test_input) is expected
