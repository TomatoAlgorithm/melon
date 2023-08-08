package p_1932_정수삼각형;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] scoreBoard = new int[501][501];
        int[][] dp = new int[501][501];

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < i; j++) {
                scoreBoard[i][j + 1] = Integer.parseInt(line[j]);
            }
        }
        dp[1][1] = scoreBoard[1][1];
        for (int i=2;i<=n;i++){
            for (int j=1;j<=i;j++){
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) + scoreBoard[i][j];
            }
        }
        int maxVal = -1;
        for(int v : dp[n]){
            maxVal = Math.max(v, maxVal);
        }
        System.out.println(maxVal);
    }
}
