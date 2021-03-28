# The problem is as follows: A dominant member in the array is one that occupies over half the positions in the array,
# for example:
#
# {3, 67, 23, 67, 67}
#
# 67 is a dominant member because it appears in the array in 3/5 (>50%) positions.
#
# Now, you are expected to provide a method that takes in an array and returns an index of the dominant member if one
# exists and -1 if there is none.
#
# Easy, right? Well, I could have solved the problem handily if it were not for the following constraints:
#
#     Expected time complexity is O(n)
#     Expected space complexity is O(1)
#
# I can see how you could solve this for O(n) time with O(n) space complexities as well as O(n^2) time with O(1)
# space complexities, but not one that meets both O(n) time and O(1) space.



