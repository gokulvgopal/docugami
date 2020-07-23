# Python Take Home Question

Welcome to the Docugami Python take home question! We also have this same question available in C# and Java, so please select the language the you are most comfortable with.

## Problem Outline and Requirements
1. Implement a disk backed queue. As a refresher, a Queue is a FIFO data structure with O(1) insert and remove operations.

1. The queue will derive from the BaseQueue abstract class. Please do not modify anything in the "base" directory.

1. The queue constructor takes an integer when it is constructed. That integer dictates the maximum number of queue nodes that can be kept in memory at any given time. All other nodes in the queue must be written to disk.

1. To get started create a venv (or a conda environment) and run "pip install -e ." from the take_home_package directory.

1. The implmentation should not use any of the built in Python collection classes (e.g. [] (Lists), collections.*, etc.) as part of the queue implementation. We understand that this makes the question somewhat contrived. 

1. Place your implemenation in the "implementation" directory. We believe that requirements.txt contains all of the necessary requirements to implement your solution. If you would like to add another requirement package to the package, please ask!

1. There is a test file in the "implementation_tests" directory. Please implement any unit tests that you feel would be helpful to test your code.

1. The code will be evaluated on the following criteria:
    1. **Correctness.** We have a private set of unit tests that we will run on the code to evaluate this.
    1. **Robustness.** Is the code "production" quality?
    1. **Readability and Organization.** Is your code easy to read? Could another developer easily make changes to your code?
    1. **Unit Tests.** Did you write a thorough set of unit tests for your queue? Did you correctly handle all of the corner cases? Maybe you thought of some tests that we missed! :)

1. Please do not use external resources to help with the algorithmic aspects of this problem. We really want to see how you think and code. That said, if you have basic questions on the functionality of Python built in libraries, feel free to find answers on the internet. To clarify, here is a good and bad example of when to use external resources:
    - **Good:** Searching Stack Overflow to understand a nuance of how the Python file apis work.
    - **Bad:** Searching Stack Overflow for how to implement a queue.

1. Please provide a README.md with your submission to describe:
    - The design choices you made and why you made them.
    - Any external resources you used for help.
    - The amount of time that it took you to write the code and test cases.

1. **Have fun!** If you have any questions, feel stuck or have any concerns, please email enghiring@docugami.com.

## Required Tools

1. Python 3.6 or greater.

2. The IDE of your choice. We recommend Visual Studio Code: https://code.visualstudio.com/Download. If you use VS Code, here are some nice extensions:
    - Python


____________________________________________________________________________________________________________________________

## Solution

### Design Architecture

The disk backed queue is implemented using two key points:
1.	Object classes for storing queue elements in memory and on disk
2.	Serializing and Deserializing the queue elements when storing to and reading from the disk

Each queue element is defined using Node class which has the attributes 'next' and 'value'. To store excess part of queue on disk, StoredQueue is defined that have only the 'head' and 'tail' attribute. StoredQueue mimics the Queue class with minimal attributes. In this way, we have a similar queue structure on disk that is easily processed. Pickle is used for serializing and deserializing the StoredQueue objects.

The number of elements that can be stored in the memory is defined by the max-in-memory attribute. Until max-in-memory, values are stored in memory as Node objects and a in-memory counter is incremented. When the queue is full, excess elements are stored directly to disk using pickle and a on-disk counter is incremented. If the max-in-memory is zero, then all elements are directly stored on to disk and on-disk counter is incremented.


### External Resources used

1. I read about file implemenation, serializing/deserializing from different websites.
2. I also referred to computer architecture and its implemenation to see how/when/what to store to disk for better performance

### Time Taken

Overall Time used comprises of:
1. Research - 2hrs
2. Coding - 1 hr
3. Testing - 1 hr

