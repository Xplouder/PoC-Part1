"""
Unit tests for Cookie Clicker Simulator
"""
import unittest
import CookieClickerSimulator
import poc_clicker_provided as provided


class TestsCookieClickerSimulator(unittest.TestCase):
    def test_ClickerState_time_until1(self):
        expected = 2.0

        obj = CookieClickerSimulator.ClickerState()
        obj.wait(45.0)
        obj.buy_item('item', 1.0, 3.5)
        result = obj.time_until(49.0)

        self.assertEqual(expected, result)

    def test_ClickerState_time_until2(self):
        expected = "Time: 45.0 Current Cookies: 44.0 CPS: 4.5 Total Cookies: " \
                   "45.0 History (length: 2): [(0.0, None, 0.0, 0.0), " \
                   "(45.0, 'item', 1.0, 45.0)]"

        obj = CookieClickerSimulator.ClickerState()
        obj.wait(45.0)
        obj.buy_item('item', 1.0, 3.5)
        result = obj.__str__()

        self.assertEqual(expected, result)

    def test_simulate_clicker(self):
        expected = "Time: 5000.0 Current Cookies: 5000.0 CPS: 1.0 Total " \
                   "Cookies: 5000.0 History (length: 1): " \
                   "[(0.0, None, 0.0, 0.0)]"
        build_info = provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]},
                                        1.15)

        result = CookieClickerSimulator.simulate_clicker(build_info,
                                                         5000.0,
                                                         CookieClickerSimulator.
                                                         strategy_none)

        self.assertEqual(expected, result.__str__())

    def test_strategy_cursor_broken1(self):
        expected = "Time: 10.0 Current Cookies: 10.0 CPS: 1.0 Total Cookies: " \
                   "10.0 History (length: 1): [(0.0, None, 0.0, 0.0)]"
        build_info = provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]},
                                        1.15)

        result = CookieClickerSimulator.simulate_clicker(build_info,
                                                         10.0,
                                                         CookieClickerSimulator.
                                                         strategy_cursor_broken)

        self.assertEqual(expected, result.__str__())

    def test_strategy_cursor_broken2(self):
        build_info = provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15)

        result = CookieClickerSimulator.simulate_clicker(build_info,
                                                         16.0,
                                                         CookieClickerSimulator.
                                                         strategy_cursor_broken)

        self.assertAlmostEqual(16.0, result.get_time())
        self.assertAlmostEqual(13.9125, result.get_cookies())
        self.assertAlmostEqual(151.0, result.get_cps())
        self.assertAlmostEqual(66.0, result._total_num_cookies)
        self.assertEqual(4, len(result.get_history()))
        self.assertIn((0.0, None, 0.0, 0.0), result.get_history())
        self.assertIn((15.0, 'Cursor', 15.0, 15.0), result.get_history())
        self.assertIn((16.0, 'Cursor', 19.837499999999999, 66.0),
                      result.get_history())

    def test_strategy_cursor_broken3(self):
        build_info = provided.BuildInfo()

        result = CookieClickerSimulator.simulate_clicker(build_info,
                                                         CookieClickerSimulator.
                                                         SIM_TIME,
                                                         CookieClickerSimulator.
                                                         strategy_cursor_broken)

        self.assertAlmostEqual(10000000000.0, result.get_time())
        self.assertAlmostEqual(6965195661.5, round(result.get_cookies(), 1))
        self.assertAlmostEqual(16.1, result.get_cps())
        self.assertAlmostEqual(153308849166.0, round(result._total_num_cookies))


if __name__ == '__main__':
    unittest.main()
