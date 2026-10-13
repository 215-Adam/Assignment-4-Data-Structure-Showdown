# Selected question (Group 4: Last-In, First-Out Logic)
#
# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
# Input: "{[(])}"
# Output: False

# Structure: a stack (a Python list using append/pop at the end).
# The most recently opened bracket must be the first one closed, which is
# exactly last-in, first-out. Each character is pushed or popped once in O(1),
# so the whole check is O(n) time and O(n) space in the worst case.

PAIRS = {")": "(", "]": "[", "}": "{"}
OPENERS = set(PAIRS.values())


def is_balanced(text):
    if not isinstance(text, str):
        raise TypeError("is_balanced expects a string")

    stack = []
    for char in text:
        if char in OPENERS:
            stack.append(char)
        elif char in PAIRS:
            # A closer with nothing open, or the wrong opener on top, fails.
            if not stack or stack.pop() != PAIRS[char]:
                return False
        # Any other character (letters, digits, spaces) is ignored.

    # Leftover openers mean something was never closed.
    return not stack


if __name__ == "__main__":
    tests = [
        ("{[()]}", True),           # example from the prompt
        ("{[(])}", False),          # example from the prompt (crossed pairs)
        ("", True),                 # empty string: nothing to unbalance
        ("()[]{}", True),           # side-by-side pairs
        ("(((", False),             # only openers
        (")))", False),             # only closers
        ("(]", False),              # mismatched types
        ("([]", False),             # unclosed opener left on stack
        ("())", False),             # extra closer
        ("if (a[0] == {b}) x()", True),  # non-bracket characters ignored
        ("abc", True),              # no brackets at all
    ]

    passed = 0
    for text, expected in tests:
        result = is_balanced(text)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        print(f"{status}: is_balanced({text!r}) -> {result} (expected {expected})")

    # Wrong data type edge cases
    for bad_input in [None, 123, ["(", ")"]]:
        try:
            is_balanced(bad_input)
            print(f"FAIL: is_balanced({bad_input!r}) did not raise TypeError")
        except TypeError:
            passed += 1
            print(f"PASS: is_balanced({bad_input!r}) raised TypeError")

    print(f"\n{passed}/{len(tests) + 3} tests passed")
