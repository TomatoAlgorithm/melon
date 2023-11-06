package p_17626_ForSquares;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] minCnt = new int[50001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        minCnt[1] = 1;

        for(int i=1;i<=n;i++){
            minCnt[i] = minCnt[1]+minCnt[i-1];
            for(int j=2;j*j<=i;j++){
                minCnt[i] = Math.min(minCnt[i],1 + minCnt[i-j*j]);
            }
        }

        System.out.println(minCnt[n]);
    }
}
