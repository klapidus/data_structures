from abc import ABC, abstractmethod
from datetime import datetime
from queue import PriorityQueue
import random
from string import ascii_uppercase
from typing import Any

import numpy as np


class BasePriorityQueue(ABC):
    @property
    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, item: Any, priority: float) -> None:
        """Inserts an element with the assigned priority."""
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> Any:
        """
        Returns the element with the highest priority
        and removes it from the queue.
        """
        raise NotImplementedError

    @abstractmethod
    def peek(self) -> Any:
        """
        Returns the element with the highest priority
        without removing it from the queue.
        """
        raise NotImplementedError

    # @abstractmethod
    # def clear(self) -> None:
    #     raise NotImplementedError


class NaivePriorityQueue(BasePriorityQueue):
    """A naive implementation."""
    def __init__(self):
        self._queue = []

    @property
    def is_empty(self):
        return len(self._queue) == 0

    @property
    def size(self) -> int:
        return len(self._queue)

    def enqueue(self, item, priority: float) -> None:
        self._queue.append((item, priority))

    def _max_priority_index(self):
        max_idx = -1
        max_priority = -1  # assume priority is always positive
        for idx, pair in enumerate(self._queue):
            _, priority = pair
            if priority > max_priority:
                max_priority = priority
                max_idx = idx
        return max_idx

    def peek(self) -> Any:
        if self.is_empty:
            return None
        mp_idx = self._max_priority_index()
        return self._queue[mp_idx]

    def dequeue(self) -> Any:
        if self.is_empty:
            return None
        mp_idx = self._max_priority_index()  # linear time complexity
        return self._queue.pop(mp_idx)


def time_queue(pq, gen_list: list):
    start = datetime.now()
    for idx in range(len(gen_list)):
        p = np.random.rand()
        npq.enqueue(gen_list[idx], p)
    for _ in range(npq.size):
        d = npq.dequeue()
    timing = (datetime.now() - start).total_seconds()
    return timing


if __name__ == "__main__":
    # pq = NaivePriorityQueue()
    # assert pq.dequeue() is None
    # pq.enqueue("item108", 0.1)
    # pq.enqueue("item7", 1.2)
    # pq.enqueue("item0", 0.01)
    # for _ in range(7):
    #     d = pq.dequeue()
    #     print(d)

    N = 1_000_0
    gen_list = [random.choice(ascii_uppercase) for _ in range(N)]

    # 1. naive pq
    npq = NaivePriorityQueue()
    timing = time_queue(npq, gen_list)
    print(f"Naive priority queue with {N} elements: {timing} seconds")
    del npq

    # 2. std library pq
    std_pq = PriorityQueue()
    start = datetime.now()
    for idx in range(len(gen_list)):
        p = np.random.rand()
        std_pq.put((p, gen_list[idx]))
    for _ in range(len(gen_list)):  # don't rely on qsize?
        d = std_pq.get()
    timing = (datetime.now() - start).total_seconds()
    print(f"Std lib priority queue with {N} elements: {timing} seconds")
    del std_pq
