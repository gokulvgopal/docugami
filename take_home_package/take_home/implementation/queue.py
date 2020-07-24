# Copyright (c) Docugami, Inc. All rights reserved.

from take_home.base.base_queue import BaseQueue
import pickle

# Node Object
class Node(object):
    def __init__(self, value=None):
        self.next = None
        self.value = value

# Queue Class for storing in the disk
class StoredQueue():
    def __init__(self):
        self.head = None
        self.tail = None

class Queue(BaseQueue):
    """ Abstract base class for queue implementations. """

    def __init__(self, max_in_memory: int, count=0, in_memory_count=0, on_disk_count=0):
        try:
            super().__init__(max_in_memory)
            if (self.max_in_memory is None) or (type(self.max_in_memory) is not int) or (self.max_in_memory < 0):
                raise ValueError("Invalid Max_in_memory. Enter a non-negative integer.")
            self._count = count
            self._in_memory_count = in_memory_count
            self._on_disk_count = on_disk_count
            self.head = None
            self.tail = None
        except:
            pass

    # Count is considered to be the sum of all elements disk and memory together
    @property
    def count(self) -> int:
        return self.on_disk_count+self.in_memory_count

    @property
    def in_memory_count(self) -> int:
        return self._in_memory_count

    @in_memory_count.setter
    def in_memory_count(self, in_memory_count):
        self._in_memory_count = in_memory_count

    @property
    def on_disk_count(self) -> int:
        return self._on_disk_count

    @on_disk_count.setter
    def on_disk_count(self, on_disk_count) -> int:
        self._on_disk_count = on_disk_count

    # Function to read/write queue objects
    def disk_file_open(self, operation: str):
        return open('queue_on_disk',operation)

    def disk_file_close(self, file):
        file.close()

    # saves the excess queue nodes in the disk
    def save_to_disk(self, node: StoredQueue):
        try:
            file = self.disk_file_open('wb')
            pickle.dump(node, file)
            self.disk_file_close(file)
        except pickle.PicklingError and FileNotFoundError and EOFError:
            return None
        except Exception as e:
            return None

    # fetch the stored queue nodes from the disk
    def fetch_from_disk(self):
        try:
            file =self.disk_file_open('rb')
            stored_queue = pickle.load(file)
            self.disk_file_close(file)
            return stored_queue
        except pickle.PicklingError and FileNotFoundError and EOFError:
            return None
        except Exception as e:
            return None

    # function that converts the node object to disk storage format(StoredQueue) and saves it to disk
    def prepare_to_save(self, node: Node):
        if self.on_disk_count == 0:
            stored_queue = StoredQueue()
            stored_queue.head = stored_queue.tail = node
        else:
            stored_queue = self.fetch_from_disk()
            stored_queue.tail.next = node
            stored_queue.tail = node
        self.on_disk_count += 1
        self.save_to_disk(stored_queue)

    # fetches a single node from the stored queue elements if they exist and stores the rest of it back to disk
    def take_from_disk(self):
        if self.on_disk_count == 0:
            return None
        else:
            stored_queue = self.fetch_from_disk()
            node = stored_queue.head
            stored_queue.head = stored_queue.head.next
            self.on_disk_count -= 1
            if self.on_disk_count > 0:
                self.save_to_disk(stored_queue)
            return node

    # Adds a node element to the queue.
    # If queue is full then excess nodes are stored in the disk
    def enqueue(self, value):
        node = Node(value)
        if self.max_in_memory > 0 and self.in_memory_count < self.max_in_memory:
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.in_memory_count += 1
        else:
            self.prepare_to_save(node)

    # removes a element from the queue (FIFO order)
    # If queue can accomodate more elements in memory and if there are elements stored in the disk,
    # then a node is transfered to memory from disk
    # If queue memory capacity is 0 when disk memory contains some element then a node element is removed from disk
    def dequeue(self) -> object:
        if self.max_in_memory > 0:
            if not self.head:
                return None
            else:
                value = self.head.value
                self.head = self.head.next
                self.in_memory_count -= 1
                if self.in_memory_count < self.max_in_memory and self.on_disk_count > 0:
                    self.enqueue(self.take_from_disk())
                return value
        else:
            node = self.take_from_disk()
            return node.value if node else node

    # function looks for the head of queue and returns the value
    # if queue memory capacity is 0, then it would look in disk for head element
    def peek(self) -> object:
        if self.max_in_memory > 0:
            if not self.head:
                return None
            else:
                return self.head.value
        else:
            if self.on_disk_count > 0:
                return self.fetch_from_disk().head.value
            else:
                return None


