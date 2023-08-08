package p_12886_돌그룹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int [] targetArray = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int tot = 0;
        for(int i = 0 ; i < 3 ; i++){
            int cur =  Integer.parseInt(st.nextToken());
            targetArray[i] = cur;
            tot+=cur;
        }

        if(tot % 3 == 0){

        }else{
            System.out.println(0);
        }

    }
}
