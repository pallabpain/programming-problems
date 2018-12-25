#!/usr/bin/env python

"""
The problem here is to find the kth smallest element in an unsorted array

This is one solution for the above problem. With the given unsorted array of
numbers, first you create min-heap and then extract the minimum k times to
get to the kth smallest element. The time complexity calculation is as follows:

Time complexity of building the min-heap = O(n)
Time complexity of extracting the minimum = O(logn)
Total = build-heap + k * extract-min => O(n + klogn)
"""


class MinHeap(object):
    """Represents a min-heap"""

    def __init__(self, num_list):
        self.heap = num_list
        self.build_heap()

    def __str__(self):
        return ",".join(str(i) for i in self.heap)

    def heapify(self, i):
        """
        Recursive method to heapify a subtree with root at a given index
        assuming that sub-trees are already heapified
        """
        left, right = 2*i + 1, 2*i + 2
        _min = i
        heap_size = len(self.heap)
        if (left < heap_size) and (self.heap[left] < self.heap[i]):
            _min = left
        if (right < heap_size) and (self.heap[right] < self.heap[_min]):
            _min = right
        if _min != i:
            self.heap[i], self.heap[_min] = self.heap[_min], self.heap[i]
            self.heapify(_min)

    def build_heap(self):
        """
        Builds a min-heap given an unsorted list of numbers
        """
        heap_size = len(self.heap)
        for i in range((heap_size-1) // 2, -1, -1):
            self.heapify(i)

    def extract_min(self):
        """Extracts and returns the root of the heap"""
        heap_size = len(self.heap)
        if heap_size == 0:
            return None
        root = self.heap[0]
        if heap_size > 1:
            self.heap[0] = self.heap[heap_size-1]
            self.heapify(0)
        return root

    def get_min(self):
        """Returns the value at the root of the heap"""
        return self.heap[0]


def get_smallest(arr, k=1):
    """Returns the k-th smallest value"""
    heap = MinHeap(arr)
    for _ in range(k-1):
        heap.extract_min()
    return heap.get_min()


if __name__ == "__main__":
    arr = [91, 2, 0, 32, 1, 8, 3, 18, 29, 4]
    print "Smallest =", get_smallest(arr, 1)
    print "2nd Smallest =", get_smallest(arr, 2)
    print "3rd Smallest =", get_smallest(arr, 3)
