"""
Merge function Unit Tests for 2048 game.
"""

import unittest

import Question10


class MyTestCase(unittest.TestCase):
    def test_brute_force(self):
        possible_elements = [0] + [2 ** x for x in range(0, 25)]

        # [pos0, pos1, pos2, pos3]

        TEST_CASES = [[],
                      [0, 2, 4, 4],
                      [0, 2, 4, 2],
                      [2, 2, 2, 2, 2],
                      [2, 4, 8, 16],
                      [0, 1, 1, 2],
                      [1, 0, 2, 0],
                      [1, 1, 1, 2],
                      [0, 0, 1, 2],
                      [1, 1, 2, 2]]

        for pos0 in possible_elements:
            for pos1 in possible_elements:
                for pos2 in possible_elements:
                    for pos3 in possible_elements:

                        test_case = [pos0, pos1, pos2, pos3]

                        original = Question10.merge_original(test_case)
                        error_mess = "Test case '" + str(
                            test_case) + "' failed."

                        try:
                            # expected1 = Question10.merge1(test_case)
                            # self.assertEqual(original, expected1, error_mess)
                            #
                            # expected4 = Question10.merge4(test_case)
                            # self.assertEqual(original, expected4, error_mess)
                            #
                            # print test_case
                            # expected18 = Question10.merge18(test_case)
                            # self.assertEqual(original, expected18, error_mess)
                            #
                            # expected12 = Question10.merge12(test_case)
                            # self.assertEqual(original, expected12, error_mess)
                            #
                            # expected35 = Question10.merge35(test_case)
                            # self.assertEqual(original, expected35, error_mess)
                            #
                            # expected57 = Question10.merge57(test_case)
                            # self.assertEqual(original, expected57, error_mess)
                            #
                            # expected127 = Question10.merge127(test_case)
                            # self.assertEqual(original, expected127, error_mess)
                            #
                            # expected130 = Question10.merge130(test_case)
                            # self.assertEqual(original, expected130, error_mess)
                            #
                            # expected159 = Question10.merge159(test_case)
                            # self.assertEqual(original, expected159, error_mess)
                            #
                            # expected189 = Question10.merge189(test_case)
                            # self.assertEqual(original, expected189, error_mess)
                            #
                            # LIMIT REACHED ####################################
                            #
                            # expected209 = Question10.merge209(test_case)
                            # self.assertEqual(original, expected209, error_mess)
                            #
                            # expected233 = Question10.merge233(test_case)
                            # self.assertEqual(original, expected233, error_mess)
                            #
                            # expected238 = Question10.merge238(test_case)
                            # self.assertEqual(original, expected238, error_mess)
                            #
                            # expected239 = Question10.merge239(test_case)
                            # self.assertEqual(original, expected239, error_mess)
                            #
                            # expected242 = Question10.merge242(test_case)
                            # self.assertEqual(original, expected242, error_mess)
                            #
                            # []
                            # expected254 = Question10.merge254(test_case)
                            # self.assertEqual(original, expected254, error_mess)
                            #
                            # expected259 = Question10.merge259(test_case)
                            # self.assertEqual(original, expected259, error_mess)
                            #
                            # [0, 0, 0, 0, 0]
                            # expected286 = Question10.merge286(test_case)
                            # self.assertEqual(original, expected286, error_mess)
                            #
                            # expected300 = Question10.merge300(test_case)
                            # self.assertEqual(original, expected300, error_mess)
                            #
                            # expected306 = Question10.merge306(test_case)
                            # self.assertEqual(original, expected306, error_mess)
                            #
                            # [2, 2, 2, 2, 2]
                            # expected324 = Question10.merge324(test_case)
                            # self.assertEqual(original, expected324, error_mess)
                            #
                            # [2, 4, 8, 16]
                            # expected326 = Question10.merge324(test_case)
                            # self.assertEqual(original, expected326, error_mess)
                            #
                            # expected347 = Question10.merge347(test_case)
                            # self.assertEqual(original, expected347, error_mess)
                            #
                            # expected351 = Question10.merge351(test_case)
                            # self.assertEqual(original, expected351, error_mess)
                            #
                            # expected352 = Question10.merge352(test_case)
                            # self.assertEqual(original, expected352, error_mess)
                            #
                            # expected355 = Question10.merge355(test_case)
                            # self.assertEqual(original, expected355,
                            #                  error_mess)
                            #
                            # expected360 = Question10.merge360(test_case)
                            # self.assertEqual(original, expected360,
                            #                  error_mess)

                            expected364 = Question10.merge364(test_case)
                            self.assertEqual(original, expected364,
                                             error_mess)

                        except IndexError:
                            self.fail(error_mess)


if __name__ == '__main__':
    unittest.main()
