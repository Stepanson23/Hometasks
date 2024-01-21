# 7. Tuple Exercise:
# Write a function that swaps the values of two tuples.

def tupl_swap(tuple1, tuple2):
    tuple1, tuple2 = tuple2, tuple1
    
    return f"{tuple2}, {tuple1}"


tuple1 = (1, 2)
tuple2 = (3, 4)

print(tupl_swap(tuple1, tuple2))