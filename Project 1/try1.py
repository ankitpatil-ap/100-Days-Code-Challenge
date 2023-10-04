def countOccur(parent, sub):
    # Convert both strings to lowercase for case-insensitive comparison
    parent_lower = parent.lower()
    sub_lower = sub.lower()

    count = 0
    start_index = 0

    while start_index < len(parent_lower):
        index = parent_lower.find(sub_lower, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + len(sub_lower)

    return count

def main():
    parent = str(input())  # Input for parent
    sub = str(input())  # Input for sub

    result = countOccur(parent, sub)
    print(result)

if __name__ == "__main__":
    main()
