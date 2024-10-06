#include <vector>

using namespace std;

class MyCircularQueue {
public:
    vector<int> queue;
    int p1;
    int p2;
    int n; // number of elements

    MyCircularQueue(int k) {
        queue = vector<int>(k);
        p1 = 0;
        p2 = -1;
        n = 0;
    }
    
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        n++;
        p2++;
        if (p2 >= queue.size()) {
            p2 = 0;
        }

        queue[p2] = value;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        n--;

        // make old data just stay as garbage data
        p1++;
        if (p1 >= queue.size()) {
            p1 = 0;
        }

        return true;
    }
    
    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return queue[p1];
    }
    
    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return queue[p2];
    }
    
    bool isEmpty() {
        return (n == 0);
    }
    
    bool isFull() {
        return (n >= queue.size());
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */

int main() {
    return 0;
}