package nl.han.ica.datastructures;

import java.util.LinkedList;

public class HANStack<T> implements IHANStack<T> {

    private LinkedList<T> stack;

    public HANStack() {
        stack = new LinkedList<>();
    }

    @Override
    public void push(T value) {
        stack.addFirst(value);
    }

    @Override
    public T pop() {
        if (stack.isEmpty()) {return null;}
        return stack.removeFirst();
    }

    @Override
    public T peek() {
        if (stack.isEmpty()) {return null;}
        return stack.getFirst();
    }
}
