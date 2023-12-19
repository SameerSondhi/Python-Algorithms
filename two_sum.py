def twoNumberSum(array, targetSum):
    # Write your code here.
    dict = {}
    for num in array:
        if targetSum - num in dict:
            return [dict[targetSum - num], num]
        else:
            dict[num] = num
    return []
