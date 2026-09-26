#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0

    while i < x:
        try:
            if "{:d}".format(my_list[i]):
                print(my_list[i], end="")
                count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
        i += 1

    print()
    return count
