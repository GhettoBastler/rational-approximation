#!/usr/bin/env python


import argparse
import math

THRESHOLDS = [0.1, 0.05, 0.01]


def approx(target):

    lower_bound = (0, 1)
    higher_bound = (1, 0)

    while True:
        numerator = lower_bound[0] + higher_bound[0]
        denominator = lower_bound[1] + higher_bound[1]

        yield (numerator, denominator)

        median = numerator/denominator

        if median < target:
            lower_bound = numerator, denominator
        elif median > target:
            higher_bound = numerator, denominator
        else:
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', help='Floating point number to approximate',
                        type=float)
    parser.add_argument('-a', '--all', help='Print every successive '
                        'approximation until the target number is reached',
                        action='store_true')

    args = parser.parse_args()

    idx = 0
    for numerator, denominator in approx(args.n):
        error = (numerator/denominator) - args.n
        if args.all:
            print(f'{numerator}/{denominator} ({error:+.2%})')
        else:
            if abs(error) < THRESHOLDS[idx]:
                print(f'{numerator}/{denominator} ({error:+.2%})')
                idx += 1
            if idx == len(THRESHOLDS):
                break


if __name__ == '__main__':
    main()
