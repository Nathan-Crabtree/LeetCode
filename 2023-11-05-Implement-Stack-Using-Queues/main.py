'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
'''

from queue import Queue

class MyStack:

    def __init__(self):
        #maxsize 0 means infinite queue
        self.queue1 = Queue(maxsize=0)
        self.queue2 = Queue(maxsize=0)

    def push(self, x: int) -> None:
        self.queue1.put(x)

    def pop(self) -> int:
        i = 0;
        print("self.queue1.size=", self.queue1.qsize())
        queue1size = self.queue1.qsize()
        while i < queue1size -1 :
            print("self.queue1.Qsize=", self.queue1.qsize())
            print("i=", i)
            val = self.queue1.get()
            print("removing ", val, " from queue1")
            print("putting ", val, " onto queue2")
            self.queue2.put(val)
            i+=1
        print("hi")
        print("self.queue1.ize=", self.queue1.qsize())
        return_val = self.queue1.get()
        print("return_val = ", return_val)
        print("bye")
        i=0
        print("self.queue2.ize=", self.queue2.qsize())
        queue2size = self.queue2.qsize()
        while i < queue2size:
            print("i=", i)
            val = self.queue2.get()
            print("REMOVING ", val, " from queue2")
            print("PUTTING ", val, " onto queue1")

            self.queue1.put(val)
            i+=1

        print("returning ", return_val)
        return return_val

    def top(self) -> int:
        i = 0;
        queue1size = self.queue1.qsize()
        print("self.queue1.size=", self.queue1.qsize())
        while i < queue1size -1 :
            val = self.queue1.get()
            self.queue2.put(val)
            i+=1
        print("hi2")
        return_val = self.queue1.get()
        print("return_val:", return_val)
        i=0
        print("self.QUEUE1.size=", self.queue1.qsize())
        queue2size = self.queue2.qsize()
        while i < queue2size:
            val = self.queue2.get()
            self.queue1.put(val)
            i+=1
        print("hi3")

        self.queue1.put(return_val)
        #print("returning ", return_val)
        return return_val


    def empty(self) -> bool:
        return self.queue1.empty()

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    #param_3 = obj.top()
    #print("EMPTY: ", obj.empty())
    #print("obj.top: ", obj.top())

    param_2 = obj.pop()
    param_5 = obj.pop()
    param_6 = obj.pop()
    print("param_2: ", param_2, " param_5: ", param_5, " param_6: ", param_6)
    print("EMPTY: ", obj.empty())

    #param_4 = obj.empty()

