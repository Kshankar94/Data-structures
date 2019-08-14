
import java.util.*; 
class MinStack {
     int minVal; 
     class minElement{
         int element;
         int min;
         public minElement(int element, int min){
             this.element  = element;
             this.min = min;
         }
         
     }
    
     Deque<minElement> data;
    /** initialize your data structure here. */
    public MinStack() {
        minVal = Integer.MAX_VALUE;
        data = new ArrayDeque<minElement>();
    }
    
    public void push(int x) {
        // if(x<=minVal){minVal = x;}
        // data.addFirst(new minElement(x,minVal));
    
        data.addFirst(new minElement(x, Math.min(x,data.isEmpty() ? x : data.peek().min)));
    }
    
    public void pop() {
        // data.removeFirst();
         //when you remove, you have to update the minElement.
           data.removeFirst();
        
    }
    
    public int top() {
         return data.peekFirst().element;
    }
    
    public int getMin() {
        return data.peekFirst().min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */