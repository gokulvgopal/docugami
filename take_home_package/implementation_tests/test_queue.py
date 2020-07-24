''' Copyright (c) Docugami, Inc. All rights reserved. '''

from take_home.implementation.queue import Queue


# Test unit to check if peek functionality works
def test_peek():
    ''' Simple test of the peek method. '''
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.peek() == 1


# Test unit to check if enqueue functionality works
def test_enqueue():
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.count == 1


# Test unit to check if dequeue functionality works
def test_dequeue():
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.dequeue() == 1 and queue.count == 0


# Test unit to check empty queue
def empty_dequeue():
    queue = Queue(10)
    assert not queue.dequeue() and queue.count == 0


# Test unit to check if excess nodes are stored in disk
def full_enqueue():
    queue = Queue(1)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.on_disk_count == 1


# test unit to check peek functionality for zero in-memory capacity
def empty_queue_peek():
    queue = Queue(0)
    assert not queue.peek()


# test unit to check enqueue functionality for zero in-memory capacity
def empty_queue_enqueue():
    queue = Queue(0)
    queue.enqueue(3)
    assert queue.on_disk_count == 1 and queue.count == 1


# test unit to check dequeue functionality for zero in-memory capacity
def empty_queue_dequeue():
    queue = Queue(0)
    assert not queue.dequeue()

# simulating an enqueue dequeue sequence and verifying queue both in memory
# and on disk
def memory_full_disk_non_zero():
    queue = Queue(5)
    queue.enqueue(3)
    queue.enqueue(7)
    assert queue.dequeue() == 3 and queue.peek() == 7
    queue.enqueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(8)
    queue.enqueue(5)
    assert queue.on_disk_count == 1
    queue.enqueue(1)
    assert queue.count == 7
    assert queue.on_disk_count == 2


# simulating an enqueue dequeue sequence with a different in-memory capacity and verifying queue both in memory
# and on disk
def memory_full_disk_zero():
    queue = Queue(4)
    queue.enqueue(3)
    queue.enqueue(7)
    assert queue.dequeue() == 3 and queue.peek() == 7
    queue.enqueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.on_disk_count == 0 and queue.count == 4
    queue.enqueue(8)
    queue.enqueue(5)
    assert not queue.on_disk_count == 1 and queue.in_memory_count == 4
    queue.enqueue(1)
    assert queue.count == 7
    assert queue.on_disk_count == 3


# simulating an enqueue dequeue sequence for zero in-memory capacity and verifying queue both in memory
# and on disk
def memory_zero_disk():
    queue = Queue(0)
    queue.enqueue(3)
    queue.enqueue(7)
    assert queue.dequeue() == 3 and queue.peek() == 7
    queue.enqueue(2)
    assert queue.on_disk_count == 2 and queue.count == 2


# Testing wrong memory-size value/ type
def none_memory_size():
    try:
        queue = Queue(None)
        queue.enqueue(1)
    except:
        print("Non integer max-in-memory test successful.")
        pass


# Testing wrong memory-size value/ type
def string_memory_size():
    try:
        queue = Queue("1")
        queue.enqueue(1)
    except:
        print("Non integer max-in-memory test successful.")
        pass


# simulating an enqueue dequeue sequence with a different in-memory capacity and verifying queue both in memory
# and on disk
def memory_full_disk_zero_diff_data():
    queue = Queue(4)
    queue.enqueue(3.3)
    queue.enqueue("b")
    assert queue.dequeue() == 3.3 and queue.peek() == "b"
    queue.enqueue(5)
    queue.enqueue("1")
    queue.enqueue(2)
    assert queue.on_disk_count == 0 and queue.count == 4
    queue.enqueue(8)
    queue.enqueue(5.5)
    assert not queue.on_disk_count == 1 and queue.in_memory_count == 4
    queue.enqueue(1)
    assert queue.count == 7
    assert queue.on_disk_count == 3


if __name__ == '__main__':
    print("Executing test cases")
    test_peek()
    test_enqueue()
    test_dequeue()
    empty_dequeue()
    full_enqueue()
    empty_queue_peek()
    empty_queue_enqueue()
    empty_queue_dequeue()
    memory_full_disk_non_zero()
    memory_full_disk_zero()
    memory_zero_disk()
    none_memory_size()
    string_memory_size()
    memory_full_disk_zero_diff_data()
    print("Test Completed.")