class MyCircularQueue {
    private int[] cQueue;
    int head;
    int tail;
    int track;
    int size;
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        cQueue = new int[k];
        size = k;
        track = 0;
        head = -1;
        tail = -1;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if(isFull()) {return false;}
        tail = (tail + 1) % cQueue.length;
        cQueue[tail] = value;
        track++;
            
			if (head == -1) {
				head = tail;
               
			}
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if(isEmpty()) return false;
        head++;
        if(head == cQueue.length) head = 0;
        track--;
        return true;
        
        
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        int result = isEmpty()? -1: cQueue[head];
        return result;
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        int result = isEmpty()? -1: cQueue[tail];
        return result;
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
         return track == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return track == size;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */