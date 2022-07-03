
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        TreeMap<String, Integer> map = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            String files = br.readLine();
            int idx = files.indexOf(".") + 1;
            if (!map.containsKey(files.substring(idx))) {
                map.put(files.substring(idx), 1);
            } else {
                map.put(files.substring(idx), map.get(files.substring(idx)) + 1);
            }
        }

        for (String s : map.keySet()) {
            System.out.println(s + " "+ map.get(s));
        }
    }
}