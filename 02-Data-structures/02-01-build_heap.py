# python2
#In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
#algorithm called HeapSort. It has guaranteed worst-case running time of O(n log n) as opposed to QuickSort's
#average running time of O(n logn). QuickSort is usually used in practice, because typically it is faster, but
#HeapSort is used for external sort when you need to sort huge files that don't fit into memory of your
#computer.

#In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
#algorithm called HeapSort. It has guaranteed worst-case running time of O(n log n) as opposed to QuickSort’s
#average running time of O(n log n). QuickSort is usually used in practice, because typically it is faster, but
#HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your
#computer.

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.n = 0

    def ReadData(self):
        n = int(raw_input("Enter number of elements: "))
        self._data = [int(s) for s in raw_input("Enter integers: ").split()]
        assert n == len(self._data)
        self.n = n

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        H = self._data
        size = self.n
        #node with minimum value
        minIndex = i
        #left child, check if it is smaller
        l = 2*(i+1)-1
        if l <= size-1 and H[l] < H[minIndex]:
            minIndex = l
        #right child, check if it is smaller
        r = 2*(i+1)
        if r <= size-1 and H[r] < H[minIndex]:
            minIndex = r
        # swap parent and smaller child nodes if any
        if not (i == minIndex):
            H[i], H[minIndex] = H[minIndex], H[i]
            self._swaps.append([i, minIndex])
            self.SiftDown(minIndex)
    
    def BuildHeap(self):
        A = self._data
        size = self.n
        for i in range(size/2-1, -1, -1):
            self.SiftDown(i)
        print A
            
    
    def Solve(self):
        self.ReadData()
        self.BuildHeap()
        #self.GenerateSwaps()
        self.WriteResponse()

heap_builder = HeapBuilder()
heap_builder.Solve()
