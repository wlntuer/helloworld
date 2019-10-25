public class Bird {
    private Integer wing = 3;

    public void moo() {
        System.out.println("鸟叫声" + wing.hashCode());
    }
}