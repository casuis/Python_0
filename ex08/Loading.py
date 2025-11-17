"""
Author: asimon (Arthur Simon)
Date: 22/10/2025 15:29:34
File: Loading.py
School: 42 Paris
"""


import sys
import time
import os

def calc_bar_length(prefix: str, suffix: str) -> int:
    term_width = os.get_terminal_size().columns
    
    # caractères réservés par tqdm (|, espaces, etc.)
    reserved = 10  
    
    bar_len = term_width - len(prefix) - len(suffix) - reserved
    if bar_len < 1:
        bar_len = 1
    
    return bar_len




def ft_tqdm(lst: range) -> None:
    '''
    This Function imitate the comportementof the tqdm function from the
    tqdm Lib  
    It waiting as parameter a range wich reprensente the total pkg and the current state
    '''
    total = len(lst)
    bar_len = int((os.get_terminal_size().columns / 100) * 70) - 10
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
