package p_2075_N번째큰수;

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
            String[] row = br.readLine().split(" ");

            for(int j = 0 ; j<n;j++){
                priorityQueue.add(Integer.parseInt(row[j]));
            }
        }

        for(int k=0;k<n-1;k++){
            priorityQueue.poll();
        }

        System.out.println(priorityQueue.poll());
    }
}
