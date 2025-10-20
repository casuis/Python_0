"""
Author: Asimon
Date: Oct 20 2025
School: 42 Paris
"""


def ft_filter(f, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    This function take a function or None and an iterable,
    than return a result where f(iterable) is True
    """
    if f is None:
        result = [item for item in iterable]
    else:
        result = [item for item in iterable if f(item)]
    return result


# def main():
#     result = ft_filter(lambda s: s.isupper(), ["TOTO", "tata"])
#     result_bis = ft_filter(lambda s: s.isupper(), ["TOTO", "tata", "COUCOU"])
#     print(f"{result}")
#     print(f"{result_bis}")


# if __name__ == "__main__":
#     main()
