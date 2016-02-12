# coding=utf-8
"""
Cookie Clicker Simulator

    Necessary commands (linux):
    > sudo apt-get install python-matplotlib
    > sudo apt-get install python-tk
"""

# Used to increase the timeout, if necessary
import math

try:
    import codeskulptor
    import simpleplot
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import SimpleGUICS2Pygame.simpleplot as simpleplot

import poc_clicker_provided as provided

codeskulptor.set_timeout(20)

# Constants
SIM_TIME = 10000000000.0
CPS_WEIGHT = 0
COST_WEIGHT = 0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_num_cookies = 0.0
        self._current_num_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0

        # Tuple element:
        # (a time, an item that was bought at that time (or None),
        # cost of the item, the total number of cookies produced by that time)
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._current_time) + \
               " Current Cookies: " + str(self._current_num_cookies) + \
               " CPS: " + str(self._current_cps) + \
               " Total Cookies: " + str(self._total_num_cookies) + \
               " History (length: " + str(len(self._history)) + "): " + \
               str(self._history)

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_num_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        :param cookies:
        """
        if self._current_num_cookies >= cookies:
            return 0.0

        diff = cookies - self._current_num_cookies
        # time rounded up
        time = math.ceil(diff / self._current_cps)
        return time

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        :param time:
        """
        if time > 0.0:
            self._current_time += time
            generated_cookies = time * self._current_cps
            self._current_num_cookies += generated_cookies
            self._total_num_cookies += generated_cookies

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        :param item_name:
        :param cost:
        :param additional_cps:
        """
        if self._current_num_cookies < cost:
            return

        self._current_num_cookies -= cost
        self._current_cps += additional_cps
        item = (self._current_time, item_name, cost, self._total_num_cookies)
        self._history.append(item)


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    :param build_info:
    :param duration:
    :param strategy:
    """
    build_info_clone = build_info.clone()
    clicker_state = ClickerState()

    while clicker_state.get_time() <= duration:
        time_left = duration - clicker_state.get_time()

        # strategy(cookies, cps, history, time_left, build_info)
        item = strategy(clicker_state.get_cookies(),
                        clicker_state.get_cps(),
                        clicker_state.get_history(),
                        time_left,
                        build_info_clone)

        if item is None:
            break

        # {"Cursor": [15.0, 0.1], ...
        elapse_time = clicker_state.time_until(build_info_clone.get_cost(item))

        if elapse_time > time_left:
            break

        clicker_state.wait(elapse_time)
        clicker_state.buy_item(item,
                               build_info_clone.get_cost(item),
                               build_info_clone.get_cps(item))
        build_info_clone.update_item(item)

    time_left = duration - clicker_state.get_time()
    if time_left > 0:
        clicker_state.wait(time_left)

    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    :param cookies:
    :param cps:
    :param history:
    :param time_left:
    :param build_info:
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    :param cookies:
    :param cps:
    :param history:
    :param time_left:
    :param build_info:
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    :param cookies:
    :param cps:
    :param history:
    :param time_left:
    :param build_info:
    """
    max_cookies = cookies + cps * time_left
    items = build_info.build_items()
    cheapest_item = None
    for item in items:
        item_cost = build_info.get_cost(item)
        if item_cost <= max_cookies:
            if cheapest_item is None:
                cheapest_item = item
            elif item_cost < build_info.get_cost(cheapest_item):
                cheapest_item = item

    return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    :param cookies:
    :param cps:
    :param history:
    :param time_left:
    :param build_info:
    """
    max_cookies = cookies + cps * time_left
    items = build_info.build_items()
    most_expensive_item = None
    for item in items:
        item_cost = build_info.get_cost(item)
        if item_cost <= max_cookies:
            if most_expensive_item is None:
                most_expensive_item = item
            elif item_cost > build_info.get_cost(most_expensive_item):
                most_expensive_item = item

    return most_expensive_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    :param cookies:
    :param cps:
    :param history:
    :param time_left:
    :param build_info:
    """

    all_items = build_info.build_items()
    max_cookies = cookies + cps * time_left
    possible_items = []

    for item in all_items:
        item_cost = build_info.get_cost(item)
        if item_cost <= max_cookies:
            possible_items.append(item)

    if len(possible_items) == 0:
        return None

    # total_cost = sum([build_info.get_cost(item) for item in possible_items])
    # total_cps = sum([build_info.get_cps(item) for item in possible_items])
    #
    # all_items_normalized = [(item,
    #                          build_info.get_cost(item) / total_cost,
    #                          build_info.get_cps(item) / total_cps)
    #                         for item in possible_items]
    #
    # all_items_by_ratio = [(item[0], item[2] * (1 / item[1]))
    #                       for item in all_items_normalized]
    #
    # all_items_by_ratio = sorted(all_items_by_ratio,
    #                             key=lambda element: element[1],
    #                             reverse=True)

    all_items_by_ratio = [(item, build_info.get_cps(item) *
                           (1.0 / build_info.get_cost(item)))
                          for item in possible_items]

    all_items_by_ratio = sorted(all_items_by_ratio,
                                key=lambda element: element[1],
                                reverse=True)

    # for i in all_items_by_ratio:
    #     print i
    # print

    return all_items_by_ratio[0][0]


def get_item_score(item, build_info, total_cost, total_cps):
    """
    Scores The item based on his attributes and the defined weights
    :param item:
    :param build_info:
    :param total_cost:
    :param total_cps:
    """
    cps_weight = 0.5
    cost_weight = 0.5

    item_cps = build_info.get_cps(item)
    item_cost = build_info.get_cost(item)

    # return cps_weight * (item_cps / total_cps) + \
    #        cost_weight * (1.0 / (item_cost / total_cost))

    return CPS_WEIGHT * (item_cps / total_cps) + \
           COST_WEIGHT * (1.0 / (item_cost / total_cost))


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    :param strategy_name:
    :param time:
    :param strategy:
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
    print state._total_num_cookies

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 500, 'Time', 'Total Cookies',
                          [history], True, _block=True)


    # global CPS_WEIGHT, COST_WEIGHT
    #
    # best_cost_weight = COST_WEIGHT
    # best_cps_weight = CPS_WEIGHT
    # max_total_cookies = float("-inf")
    # max = 1000.0
    # lista = []
    #
    # for val in range(99, int(max) + 1):
    #     CPS_WEIGHT = val / max
    #     COST_WEIGHT = (max - val) / max
    #
    #     state = simulate_clicker(provided.BuildInfo(), time, strategy)
    #     lista.append(state._total_num_cookies)
    #     if state._total_num_cookies > max_total_cookies:
    #         max_total_cookies = state._total_num_cookies
    #         best_cost_weight = COST_WEIGHT
    #         best_cps_weight = CPS_WEIGHT
    #
    # print best_cost_weight, best_cps_weight
    # print max_total_cookies

    # print
    # for i in lista:
    #     print i


def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)


run()
