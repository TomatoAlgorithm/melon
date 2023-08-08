package p_4358_생태학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//        PriorityQueue<String> pq = new PriorityQueue<>();
        Map<String, Integer> map = new HashMap<>();

        String input = "";
        int tot = 0;
        while(true) {
            if((input = br.readLine()) == null) break;

            tot++;
            map.put(input, map.getOrDefault(input,0)+1);
        }

        StringBuilder sb = new StringBuilder();
        List<String> keySet = new ArrayList<>(map.keySet());
        Collections.sort(keySet);
        for (String s:
             keySet) {
            int cnt = map.get(s);
            double per = (double)cnt/(double)tot;
            sb.append(String.format("%s %.4f\n",s,per*100));
//            System.out.println(String.format("%s %.4f",s,(float)(map.get(s)/tot)));
        }
        System.out.println(sb);
    }
}
