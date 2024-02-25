'''
https://leetcode.com/problems/implement-queue-using-stacks/
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        i = 0
        stack1len = self.stack1.__len__()
        while i < stack1len:
            num = self.stack1.pop()
            #print ("popping ", num, " off stack1")
            #print ("appending ", num, " to stack2")

            self.stack2.append(num)
            i+=1
        return_val = self.stack2.pop()

        i=0
        stack2len = self.stack2.__len__()
        while i < stack2len:
            num = self.stack2.pop()
            #print ("POPPING ", num, " off stack2")
            #print ("APPENDING ", num, " to stack1")
            self.stack1.append(num)
            i+=1
        return return_val

    def peek(self) -> int:
        i = 0
        stack1len = self.stack1.__len__()
        while i < stack1len:
            num = self.stack1.pop()
            print ("popping ", num, " off stack1")
            print ("appending ", num, " to stack2")
            self.stack2.append(num)
            #self.stack2.append(self.stack1.pop())
            i+=1
        return_val = self.stack2.pop()
        print("return_val: ", return_val)
        print("Appending ", return_val, " to stack1")
        self.stack1.append(return_val)
        i = 0
        stack2len = self.stack2.__len__()
        while i < stack2len:
            num = self.stack2.pop()
            print("popping ", num, " off stack2")
            print("appending ", num, " to stack1")
            self.stack1.append(num)
            #self.stack1.append(self.stack2.pop())
            i += 1

        return return_val

    def empty(self) -> bool:
        return self.stack1.__len__() <= 0

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    myQueue.push(4)
    print(myQueue.pop())
    myQueue.push(5)
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())

    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())

