package p_14425_문자열집합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");

        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);

        Set<String> Containers = new HashSet<>();
        int cnt = 0;
        for(int i =0 ; i<n;i++){
            String word = br.readLine();

            Containers.add(word);
        }
        for(int i=0;i<m;i++){
            String word = br.readLine();
            if(Containers.contains(word)) cnt++;
        }

        System.out.println(cnt);
    }
}
