from abc import ABC, abstractmethod
from datetime import datetime
from queue import PriorityQueue
import random
from string import ascii_uppercase
from typing import Any

import numpy as np

from heap import Heap


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


class HeapPriorityQueue(Heap, BasePriorityQueue):
    """Implemented using a heap."""
    def __init__(self):
        super().__init__()

    def enqueue(self, priority: float) -> None:
        self.insert(priority)

    def peek(self) -> Any:
        return self.show_top()

    def dequeue(self) -> Any:
        return self.remove_top()

def time_queue(pq, gen_list: list):
    start = datetime.now()
    for idx in range(len(gen_list)):
        p = np.random.rand()
        pq.enqueue(gen_list[idx], p)
    for _ in range(npq.size):
        d = pq.dequeue()
    timing = (datetime.now() - start).total_seconds()
    return timing


if __name__ == "__main__":

    N = 4_000_0
    gen_list = [random.choice(ascii_uppercase) for _ in range(N)]

    # 1. naive pq
    npq = NaivePriorityQueue()
    timing = time_queue(npq, gen_list)
    print(f"Naive priority queue with {N} elements: {timing} seconds")
    del npq

    # 2. heap-based pq
    hpq = HeapPriorityQueue()
    start = datetime.now()
    for idx in range(len(gen_list)):
        p = np.random.rand()
        hpq.enqueue(p)  # TODO
    #for _ in range(npq.size):  # TODO
    for _ in range(len(gen_list)):  # TODO
        d = hpq.dequeue()
    timing = (datetime.now() - start).total_seconds()
    print(f"Heap-based priority queue with {N} elements: {timing} seconds")
    del hpq

    # 3. std library pq
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

