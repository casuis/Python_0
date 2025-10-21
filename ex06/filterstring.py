"""
Author: asimon (Arthur Simon)
Date: 20/10/2025 16:50:43
File: filterstring.py
School: 42 Paris
"""

import sys


def main():
    try:
        assert len(sys.argv) == 3, "Wrong number of arguments"
        assert len(sys.argv[1]) > 0, "First argument can't be an empty string"
        assert sys.argv[2].isdigit() and int(sys.argv[2]) >= 0, (
            "Second argument must be a positiv integer"
        )
        result = (lambda S, N: [item for item in S if len(item) >= N])(
            sys.argv[1].split(), int(sys.argv[2])
        )
        print(f"{result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return 1


if __name__ == "__main__":
    main()
