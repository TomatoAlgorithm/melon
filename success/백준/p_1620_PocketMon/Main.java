package p_1620_PocketMon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");

        Map<Integer,String> StringDogam = new HashMap<>();
        Map<String ,Integer> IntDogam = new HashMap<>();

        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);


        for (int i = 0; i < n; i++) {
            String pocketMon = br.readLine();
            StringDogam.put(i+1,pocketMon);
            IntDogam.put(pocketMon,i+1);
        }
        for (int i = 0; i < m; i++) {
            String question = br.readLine();
            boolean isDigit = isInteger(question);

            if(isDigit){
                System.out.println(StringDogam.get(Integer.parseInt(question)));
            }else{
                System.out.println(IntDogam.get(question));
            }
        }
    }

    public static boolean isInteger(String strValue) {
        try {
            Integer.parseInt(strValue);
            return true;
        } catch (NumberFormatException ex) {
            return false;
        }
    }
}
