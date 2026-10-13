"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

# Justification: A set is the best fit because it stores only unique values and
# supports average O(1) membership checks, so we can tell instantly whether an
# ID has already been seen. We loop through the IDs once, doing an O(1) lookup
# and an O(1) insert per item, for O(n) time and O(n) extra space overall
# (compared to O(n^2) if we compared every pair using a list).
def has_duplicates(product_ids):
    seen = set()
    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque


# Justification: Tasks are processed first-in, first-out, so a queue is the
# natural fit; Python's collections.deque is a double-ended queue built for
# fast operations at both ends. add_task uses append() (O(1)) and
# remove_oldest_task uses popleft() (O(1)), whereas list.pop(0) would be O(n)
# because every remaining element must shift left.
class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None
        return self.tasks.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

# Justification: A set automatically ignores duplicate values, so it holds
# exactly the distinct values seen in the stream. add() is an average O(1) set
# insertion, and get_unique_count() is O(1) because len() on a set is stored
# rather than recomputed; memory grows with the number of unique values, O(u).
class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


if __name__ == "__main__":
    # Problem 1 tests
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))       # False
    print(has_duplicates([]))                    # False

    # Problem 2 tests
    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    print(task_queue.remove_oldest_task())  # Email follow-up
    print(task_queue.remove_oldest_task())  # Code review
    print(task_queue.remove_oldest_task())  # None (empty queue)

    # Problem 3 tests
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())  # 2
