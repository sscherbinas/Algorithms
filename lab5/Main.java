import java.util.ArrayList;
import java.util.List;

public class Main {
    private int answer = Integer.MAX_VALUE;
    private List<String> fivePowers;

    public int getmin(String string) {
        final char[] arr = string.toCharArray();
        fivePowers = new ArrayList<>();
        long number = 1L;
        while (true) {
            final String tempStr = Long.toBinaryString(number);
            if (tempStr.length() > 50) {
                break;
            }
            fivePowers.add(tempStr);
            number *= 5;
        }
        dfs(arr, 0, 0);
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

    private void dfs(char[] array, int value, int weight) {
        if (value == array.length) {
            answer = Math.min(weight, answer);
            return;
        }
        for (int i = 0; i < fivePowers.size(); i++) {
            String five = fivePowers.get(i);
            if (array.length - value < five.length()) {
                break;
            }
            if (isMatching(array, value, five)) {
                dfs(array, value + five.length(), weight + 1);
            }
        }
    }

    private boolean isMatching(char[] array, int value, String binaryFive) {
        for (int i = 0; i < binaryFive.length(); i++) {
            if (array[value + i] != binaryFive.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(new Main().getmin("1111101"));
    }
}