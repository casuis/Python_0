"""
Author: asimon (Arthur Simon)
Date: 20/10/2025 16:50:43
File: filterstring.py
School: 42 Paris
"""

import sys
from ft_filter import ft_filter 


def ft_filter_string(S: str, N: int):
    string_format = S.split()
    result = [item for item in string_format if lambda s: len(s) >= N]
    return result


def main():
    try:
        assert len(sys.argv) == 3, "Wrong number of arguments"
        assert len(sys.argv[1]) > 0, "First argument can't be an empty string"
        assert sys.argv[2].isdigit() and int(sys.argv[2]) >= 0, "Second argument must be a positiv integer"
        result = ft_filter_string(sys.argv[1], int(sys.argv[2]))
        print(f"result: {result}")
    except AssertionError as e:
        sys.stderr(e)
    return


if __name__ == "__main__":
    main()