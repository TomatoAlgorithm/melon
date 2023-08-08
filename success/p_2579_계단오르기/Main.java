package p_2579_계단오르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] scoreArr = new int[301];
        int[] dp = new int[301];

        for (int i = 1; i <= n; i++) {
            scoreArr[i] = Integer.parseInt(br.readLine());
        }

        dp[1] = scoreArr[1];
        dp[2] = scoreArr[1] + scoreArr[2];

        for (int i = 3; i <= n; i++) {
            int maxValue = Math.max(dp[i - 2] + scoreArr[i], dp[i - 3] + scoreArr[i - 1] + scoreArr[i]);
            dp[i] = maxValue;
        }

        System.out.println(dp[n]);
    }
}
