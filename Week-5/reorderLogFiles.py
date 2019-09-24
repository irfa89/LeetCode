"""
937. You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.
"""

import unittest


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        num_log , str_log = [],[]

        for log in logs:
            if log.isalpha():
                str_log.append(log)
            else:
                num_log.append(log)

        def util(x):
            temp = x.split()
            return (" ".join(temp[1:]),temp[0])

        str_log = sorted(str_log,key=util)

        return str_log + num_log


class Test_Program(unittest.TestCase):

    def setUp(self):
        self.sol =  Solution()

    def test_case_1(self):
        result = self.sol.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
        self.assertEquals(result,["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])


if __name__ == "__main__":
    unittest.main()