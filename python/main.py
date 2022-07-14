def fibonacci(position):
    print("Getting fibonacci number at position {}...".format(position))

    # Check if position is 0 (last value). If so, return.
    if position <= 1:
        return position

    # Otherwise, return fibonacci of previous two values;
    # that is (position - 1 and position - 2)
    return fibonacci(position - 2) + fibonacci(position - 1)


def main():
    value = fibonacci(8)
    print("Fibonacci value at position {0} is: {1}".format(5, value))


if __name__ == "__main__":
    main()
