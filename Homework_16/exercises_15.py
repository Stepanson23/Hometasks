# 15. Multiple Exceptions:
# Write a function that performs the following tasks: Accepts a list and an index as input.
# Attempts to access the element at the given index in the list. Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not.
def access_element(numbers, index):
    try:
        element = numbers[index]
        print(f"Element of index {index}: {element}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range.")
    finally:
        print("Task completed")


numbers = [1, 2, 3, 4, 5, 6, 7]

access_element(numbers, 3)
access_element(numbers, 6)
