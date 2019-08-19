import unittest


# O(logn) | O(1)
def twoNumberSum(array,targetSum):
    array.sort()
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:
        for number in array:
            current_sum = array[left_pointer] + array[right_pointer]
            if current_sum == targetSum:
                return [array[left_pointer],array[right_pointer]]
            else:
                if current_sum > targetSum:
                    right_pointer -= 1
                else :
                    left_pointer += 1

    return []


class Test_Program(unittest.TestCase):

    def test_case_1(self):
        result = twoNumberSum([4,6,1],5)
        self.assertEquals(result,[1,4])

    def test_case_2(self):
        result = twoNumberSum([-4,-1,1,3,5,6,8,11],10)
        self.assertEquals(result,[-1,11])



if __name__ == "__main__":
    unittest.main()