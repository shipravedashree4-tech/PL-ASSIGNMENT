class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(f"Pushed {value} onto the stack.")

    def safe_pop(self):
        if not self.items:
            print("Stack is empty, nothing to pop.")
            return None
        return self.items.pop()

    def display(self):
        print("Current stack:", self.items)


def main():
    stack_obj = Stack()

    stack_obj.safe_pop()
    stack_obj.push(10)
    stack_obj.push(20)
    stack_obj.display()
    print("Popped item:", stack_obj.safe_pop())
    stack_obj.display()


if __name__ == "__main__":
    main()