from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)
        print(f"Enqueued {value}.")

    def safe_dequeue(self):
        if not self.items:
            print("Queue is empty, cannot dequeue.")
            return None
        return self.items.popleft()

    def display(self):
        print("Current queue:", list(self.items))


def main():
    queue_obj = Queue()

    queue_obj.safe_dequeue()
    queue_obj.enqueue(10)
    queue_obj.enqueue(20)
    queue_obj.display()
    print("Dequeued item:", queue_obj.safe_dequeue())
    queue_obj.display()


if __name__ == "__main__":
    main()