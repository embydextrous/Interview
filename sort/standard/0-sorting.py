'''
Other sorting algorithms:

1 - BogoSort - generate a permutation and check if it is sorted or not.
    O(inf) worst case [sorted permutation never generated], 
    O(n) best case [first permutation is sorted] and O(n * n!) in average case.
    # https://www.geeksforgeeks.org/bogosort-permutation-sort/

2 - TreeSort - Insert elements of array in a BST and traverse in inorder fashion and fill the array.
    Time Complexity - 
    O(n^2) (can be improved to O(nlogn) with balanced BSTs) - Already sorted or reverse sorted
    Average case and best case (forms a height balanced BST) is O(nlogn)
    Space Complexity - O(n)
    # https://www.geeksforgeeks.org/tree-sort/

3 - SleepSort - sleep for time proportional to value. Indeterministic due to CPU Scheduling of threads.
    # https://www.geeksforgeeks.org/sleep-sort-king-laziness-sorting-sleeping/
'''