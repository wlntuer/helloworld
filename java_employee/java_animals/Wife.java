public class Wife {
    public void listen(Bird bird) {
        bird.moo();
    }

    /*
     * 这时多态就很好的体现了，你妻子想听鸟叫，无论什么鸟都可以给她，但是你想让她和鹦鹉
     * 说话，你就买了一只鹦鹉传给listen方法，结果你妻子听到了鹦鹉的叫声，程序输出：鹦 鹉的叫声
     */
    public static void main(String[] args) {
        new Wife().listen(new Parrot());
    }
}