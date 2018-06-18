class Queue:
    def __init__(self):
            self.queue = []
    def isEmpty(self):
        return self.queue == []

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def queueLength(self):
        return len(self.queue)


queue = Queue()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
print("The queue is empty? => {}\n".format(queue.isEmpty()))
print("The size of the queue is => {}\n".format(queue.queueLength()))
print("The item that can be dequeued is => {}\n".format(queue.peek()))
print("The dequeued item is => {}\n".format(queue.deQueue()))
print("The queue is empty? => {}\n".format(queue.isEmpty()))
print("The size of the queue is => {}\n".format(queue.queueLength()))
print("The item that can be dequeued is => {}\n".format(queue.peek()))
queue.enQueue(5)
queue.enQueue(6)
print("The queue is empty? => {}\n".format(queue.isEmpty()))
print("The size of the queue is => {}\n".format(queue.queueLength()))
print("The item that can be dequeued is => {}\n".format(queue.peek()))
print("The dequeued item is => {}\n".format(queue.deQueue()))
