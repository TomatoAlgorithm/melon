package p_11279_최대힙;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        for(int i=0;i<n;i++){
            int x = Integer.parseInt(br.readLine());

            if(x == 0){
                if(priorityQueue.size() == 0){
                    System.out.println(0);
                }else{
                    System.out.println(priorityQueue.poll());
                }
            }
            else{
                priorityQueue.add(x);
            }
        }

    }
}
