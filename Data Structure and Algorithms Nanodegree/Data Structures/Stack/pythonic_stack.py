class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


if __name__ == '__main__':
    MyStack = Stack()

    MyStack.push("Web Page 1")
    MyStack.push("Web Page 2")
    MyStack.push("Web Page 3")

    print(MyStack.items)

    MyStack.pop()
    MyStack.pop()

    print("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

    MyStack.pop()

    print("Pass" if (MyStack.pop() == None) else "Fail")
