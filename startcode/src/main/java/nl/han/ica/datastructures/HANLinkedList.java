package nl.han.ica.datastructures;

public class HANLinkedList<T> implements IHANLinkedList<T> {
    private T[] data;
    private int size;
    private static final int MAX_SIZE = 100;

    public HANLinkedList() {
        data = (T[]) new Object[MAX_SIZE];
        size = 0;
    }

    @Override
    public void addFirst(T value) {
        if (size >= MAX_SIZE) throw new IllegalStateException("List is full");
        for (int i = size; i > 0; i--) { //Alles een stap naar rechts
            data[i] = data[i - 1];
        }
        data[0] = value;
        size++;
    }

    @Override
    public void clear() {
        for (int i = 0; i < size; i++) {
            data[i] = null;
        }
        size = 0;
    }

    @Override
    public void insert(int index, T value) {
        if (index < 0 || index > size) throw new IndexOutOfBoundsException();
        if (size >= MAX_SIZE) throw new IllegalStateException("List is full");
        for (int i = size; i > index; i--) { //Alles rechts van de index een stap naar rechts
            data[i] = data[i - 1];
        }
        data[index] = value;
        size++;
    }

    @Override
    public void delete(int pos) {
        if (pos < 0 || pos >= size) throw new IndexOutOfBoundsException();
        for (int i = pos; i < size - 1; i++) { //Alles na de pos een stap naar links
            data[i] = data[i + 1];
        }
        data[size - 1] = null;
        size--;
    }

    @Override
    public T get(int pos) {
        if (pos < 0 || pos >= size) throw new IndexOutOfBoundsException();
        return data[pos];
    }

    @Override
    public void removeFirst() {
        if (size == 0) throw new IllegalStateException("List is empty");
        delete(0);
    }

    @Override
    public T getFirst() {
        if (size == 0) throw new IllegalStateException("List is empty");
        return data[0];
    }

    @Override
    public int getSize() {
        return size;
    }
}