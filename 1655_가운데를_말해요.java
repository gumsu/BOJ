
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        PriorityQueue<Integer> left = new PriorityQueue<>();     // 최대힙
        PriorityQueue<Integer> right = new PriorityQueue<>();    // 최소힙

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());

            if (left.size() == right.size()) {
                left.add(-x);
            } else {
                right.add(x);
            }

            if (!left.isEmpty() && !right.isEmpty() && -left.peek() > right.peek()) {
                int left_temp = -left.poll();
                int right_temp = right.poll();

                left.add(-right_temp);
                right.add(left_temp);
            }

            sb.append(-left.peek()).append("\n");
        }
        System.out.println(sb);
    }
}