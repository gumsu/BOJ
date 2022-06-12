import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] people = new int[n];

        for (int i = 0; i < n; i++) {
            people[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(people);
        // 팁의 최댓값은 100,000 이므로 long 
        long res = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (people[i] - (n-i-1) < 0) break;
            res += people[i] - (n-i-1);
        }
        System.out.println(res);
    }
}