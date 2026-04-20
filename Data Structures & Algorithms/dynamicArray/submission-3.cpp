class DynamicArray {
public:

    int * arr;
    int length;
    int capacity;

    DynamicArray(int capacity) {
        arr = new int[capacity];
        length = 0;
        this->capacity = capacity;
    }

    ~DynamicArray() { // Destructor to deallocate memory
        delete[] arr;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        if (i >= 0 && i < length)
        {
            arr[i] = n;
        }
    }

    void pushback(int n) {
        if (length == capacity)
        {
            resize();
        }
        arr[length] = n;
        length++;
    }

    int popback() {
        if (length > 0)
        {
            length--;
        }
        return arr[length];
    }

    void resize() {
        capacity = capacity * 2;
        int * newArr = new int[capacity];
        for (int i = 0; i < length; i++)
        {
            newArr[i] = arr[i];
        } 
        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
