"""
Author: asimon (Arthur Simon)
Date: 22/10/2025 15:29:34
File: Loading.py
School: 42 Paris
"""


import sys
import time


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_len = 89
    start = time.time()
    for i in lst:
        percent = (i + 1) / total
        filled = int(bar_len * percent)
        bar = '█' * filled + ' ' * (bar_len - filled)
        elapsed = time.time() - start
        eta = ((elapsed / (i + 1)) * (total - (i + 1)))

        sys.stdout.write((
            f"\r{percent * 100:3.0f}%"
            f"|{bar}| {i+1}/{total} |"
            f"{eta:5.1f}s"
        ))
        sys.stdout.flush()
        yield i
    print()
    return
