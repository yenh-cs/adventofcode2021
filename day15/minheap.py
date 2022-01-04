def heapify(heap, index):
    parent = int(index/2)
    if parent != 0 and heap[parent] > heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        heapify(heap, index)

def get_min(heap):
    return heap[1]

def extract_min(heap):
    heap[1], heap[len(heap) - 1] = heap[len(heap) - 1], heap[1] 
    min = heap.pop()
    sink(heap, 1)
    return min


def sink(heap, index):
    left = index * 2
    right = index * 2 + 1
    smallest = index
    
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left

    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right

    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        sink(heap, smallest)


def main():
    original = [19, 25, 1, 17, 3, 7, 2, 100, 26]
    print(original)
    heap = []
    heap.append(None)

    size = len(original)
    for i in range(size):
        index = i + 1
        heap.append(original[i])
        heapify(heap, index)

    print(heap)

    while len(heap) > 1:
        print(extract_min(heap))

if __name__ == '__main__':
    main()
