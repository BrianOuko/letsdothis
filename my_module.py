print ('IMPORTED MODULE SUCCESSFULLY!')
test = 'test string'

def find_index(to_search, target):#args are a list and target value
    """finds index of a value ina sequence"""
    for i, value in enumerate(to_search):
        if value==target:
            return i
    return -1
 
print(find_index([1,2,3,4,5,6], 4))