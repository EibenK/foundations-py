"""
Creates binary search algorithm in Python

Notes for code review:
    - include git tagging (semantic versions)
    - comments explaining each function
    - Test cases for different types of binary searches
"""

class BinarySearch:
    def __init__(self):
        pass

    def search(self, data, key):
        # define boundaries
        left = 0
        right = len(data) - 1

        # while left <= right continue
        while(left <= right):
            # define mid point 
            mid = (left + right)// 2

            # if data[mid] is the key return idx where key exists
            if data[mid] == key:
                return mid
            
            # if data[mid] is less than key, change left and move mid
            elif data[mid] < key:
                left = mid + 1
                
            # if data[mid] is greater than key, change right and move mid
            else:
                right = mid - 1

        # return -1 if key not found
        return -1


if __name__ == "__main__":
    # test data
    data = [1,2,3,4,5,6,7]
    key = 7
    
    # object creation
    bs = BinarySearch()
    result = bs.search(data, key)

    print("Key found within data") if result != -1 else print("Key not found within data")
