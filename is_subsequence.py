def isValidSubsequence1(array, sequence):
    # Write your code here.
    i = 0
    k = 0

    for i, element in enumerate(array):
        if k < len(sequence) and element == sequence[k]:
            k += 1

    return k == len(sequence)

# Using pointers
def isValidSubsequence2(array, sequence):
    # Write your code here.
    array_index = 0
    sequence_index = 0

    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)
