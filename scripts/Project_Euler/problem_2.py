def fibonacci_sequence_below(n):
    a=1
    b=2
    sequence = [1, 2]
    while a+b < n:
        sequence.append(a+b)
        a, b = b, a+b

    return sequence


if __name__ == "__main__":
    print(sum(x for x in fibonacci_sequence_below(4000001) if (x % 2 == 0)))
