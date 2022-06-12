import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] lope = new int[n];
        for (int i = 0; i < n; i++) {
            lope[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(lope);

        int max = 0;
        for (int i = n-1; i >= 0; i--) {
            if (lope[i] * (n - i) > max) {
                max = lope[i] * (n - i);
            }
        }

        System.out.println(max);
    }
}