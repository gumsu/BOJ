import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int money = Integer.parseInt(br.readLine());
        int[] machineDuck = new int[14];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < machineDuck.length; i++) {
            machineDuck[i] = Integer.parseInt(st.nextToken());
        }

        int jh_money = money;
        int sm_money = money;
        int jh_stock = 0;
        int sm_stock = 0;
        int jh_res = 0;
        int sm_res = 0;

        // 준현
        for (int i : machineDuck) {
            if (jh_money >= i) {
                jh_stock += jh_money / i;
                jh_money %= i;
            }
        }

        // 성민
        for (int i = 0; i < machineDuck.length - 3; i++) {
            // buy
            if (machineDuck[i] > machineDuck[i + 1] && machineDuck[i + 1] > machineDuck[i + 2]) {
                sm_stock += sm_money / machineDuck[i + 3];
                sm_money = sm_money % machineDuck[i + 3];

                // sell
            } else if (machineDuck[i] < machineDuck[i + 1] && machineDuck[i + 1] < machineDuck[i + 2]) {
                sm_money += sm_stock * machineDuck[i + 3];
                sm_stock = 0;
            }
        }

        jh_res = jh_money + (machineDuck[13] * jh_stock);
        sm_res = sm_money + (machineDuck[13] * sm_stock);

        if (jh_res > sm_res) {
            System.out.println("BNP");
        } else if (jh_res < sm_res) {
            System.out.println("TIMING");
        } else {
            System.out.println("SAMESAME");
        }
//        System.out.println("sm_res = " + sm_res);
//        System.out.println("jh_res = " + jh_res);
    }
}