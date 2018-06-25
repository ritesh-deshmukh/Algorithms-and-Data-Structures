class Heap(object):
    heap_size = 10
    def __init__(self):
        self.heap = [0] * self.heap_size
        self.current_position = -1

    def insert(self, item):
        if self.isFull():
            print("HEap is full")
            return
        self.current_position += 1
        self.heap[self.current_position] = item
        self.fixUp(self.current_position)

    def fixUp(self, index):
        parentIndex = int((index-1)/2)

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            parentIndex = int((index - 1) / 2)

    def heapsort(self):
        arr = []
        for i in range(0, self.current_position + 1):
            temp = self.heap[0]
            arr.append(temp)
            # print("{}".format(temp))
            self.heap[0] = self.heap[self.current_position - i]
            self.heap[self.current_position - i] = temp
            self.fixDown(0, self.current_position - i - 1)
        print("Ascending order = {}".format(arr[::-1]))
        print("Descending order = {}".format(arr))

    def fixDown(self, index, upto):
        while index <= upto:
            leftChild = 2*index+1
            rightChild = 2*index+2

            if leftChild < upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                index = childToSwap
            else:
                break


    def isFull(self):
        if self.current_position == Heap.heap_size:
            return True
        else:
            return False


hp = Heap()

hp.insert(10)
hp.insert(-20)
hp.insert(0)
hp.insert(2)

hp.heapsort()