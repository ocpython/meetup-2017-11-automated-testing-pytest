# See https://redd.it/76qk58


def cannibal_calculator(numbers, queries):
    """
    An integer can consume a lower valued integer to increment its value by 1, regardless of the value of the consumed
    integer.  An integer may only be consumed once.

    Args:
        numbers: A list of integers.  Can contain duplicates.
        queries: A list of integers of target numbers.

    Returns:
        A dictionary with the input query integers as keys and the maximum amount of integers that can reach the target
        number as values.
    """

    results = {}
    sorted_numbers = sorted(numbers, reverse=True)

    for query in queries:

        results[query] = 0
        available = len(sorted_numbers)

        for n in range(len(sorted_numbers)):

            if available:

                if sorted_numbers[n] >= query:
                    results[query] += 1
                    available -= 1

                else:
                    difference = query - sorted_numbers[n]

                    if any(thing < sorted_numbers[n] for thing in sorted_numbers[n + 1:]) and available > difference:
                        results[query] += 1
                        available -= difference + 1

            else:
                break

    return results


if __name__ == '__main__':
    # r = cannibal_calculator([21, 9, 5, 8, 10, 1, 3], [10, 15])
    # r = cannibal_calculator([3, 3, 3, 2, 2, 2, 1, 1, 1], [4])
    # r = cannibal_calculator([3, 3, 3, 3], [4])
    r = cannibal_calculator([1, 2, 3, 4], [5])
    print(r)
