import numpy as np


#            43/1
#     27/2         24/3
#  18/4  14/5    3/6  (  )
# TODO: flexible topmin-topmax
class Heap:
    def __init__(self):
        self.ar = [None]  # indexing from 1

    @property
    def size(self) -> int:
        return len(self.ar) - 1

    @property
    def is_empty(self) -> int:
        if len(self.ar) == 1:
            return True
        else:
            return False

    def _swap(self, idx1, idx2):
        tmp = self.ar[idx1]
        self.ar[idx1] = self.ar[idx2]
        self.ar[idx2] = tmp

    def insert(self, el):
        self.ar.append(el)
        # sift up
        idx = len(self.ar) - 1
        while idx > 1:
            parent_idx = idx // 2
            if self.ar[parent_idx] >= self.ar[idx]:  # heap is fine
            #if self.ar[parent_idx] <= self.ar[idx]:
                break
            self._swap(idx, parent_idx)
            idx = parent_idx

    def show_top(self):
        if len(self.ar) == 1:
            return None
        else:
            return self.ar[1]

    def remove_top(self):

        if len(self.ar) == 1:
            return None
        if len(self.ar) == 2:
            return self.ar.pop(1)

        top_el = self.ar[1]
        self.ar[1] = self.ar.pop(-1)
        # sift down
        idx = 1
        while True:
            child1_idx = 2 * idx
            try:
                child1_val = self.ar[child1_idx]
            except IndexError:
                break

            child2_idx = 2 * idx + 1
            try:
                child2_val = self.ar[child2_idx]
            except IndexError:
                child2_val = None

            child_idx = child1_idx
            if child2_val is not None:
                if child2_val > child1_val:
                #if child2_val < child1_val:
                    child_idx = child2_idx

            if self.ar[child_idx] <= self.ar[idx]:  # heap is fine
            #if self.ar[child_idx] >= self.ar[idx]:
                break
            self._swap(idx, child_idx)
            idx = child_idx
        return top_el


if __name__ == "__main__":
    N = 20
    h = Heap()
    for _ in range(N):
        h.insert(np.random.randint(1000))
    #print(h.ar)
    for _ in range(N):
        top = h.remove_top()
        print(top)
    #print(h.ar)
