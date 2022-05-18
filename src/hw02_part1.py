def matrix():
    return [[col for col in range(1, 6)] for _ in range(5)]


if __name__ == "__main__":
    m = matrix()
    # regular print
    print(m)
    # pretty print
    print("\n".join([" ".join([str(col) for col in row]) for row in m]))
