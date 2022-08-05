import random

num = [random.randint(1, 1000) for i in range(100)]
a = int(input('Increasing 1\nWaning 2\n'))  # Sort type selection


def quick_sort(s):
    if len(s) <= 1:
        return s
    else:
        piv = random.choice(s)

    more = [x for x in s if x > piv]    # New sorted list
    less = [x for x in s if x < piv]
    eqv = [x for x in s if x == piv]

    if a == 1:
        return quick_sort(less) + eqv + quick_sort(more)
    else:
        return quick_sort(more) + eqv + quick_sort(less)


if __name__ == '__main__':
    print(quick_sort(num))