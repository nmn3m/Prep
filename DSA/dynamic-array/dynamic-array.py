import ctypes


class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.n] = value
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise IndexError("Pop from empty array")

        value = self.array[self.n - 1]
        self.array[self.n - 1] = None
        self.n -= 1

        if self.n > 0 and self.n == self.capacity // 4:
            self._resize(self.capacity // 2)

        return value

    def remove(self, value):
        if self.n == 0:
            raise IndexError("Removing from empty list")

        for i in range(self.n):
            if self.array[i] == value:
                for j in range(i, self.n - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.n - 1] = None
                self.n -= 1

                if self.n > 0 and self.n == self.capacity // 4:
                    self._resize(self.capacity // 2)
                return
        raise ValueError(f"{value} not found in array")


if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(arr.pop())
    print(arr[0])
    print(arr.remove(10))

    try:
        arr.remove(100)
    except ValueError as e:
        print(e)
