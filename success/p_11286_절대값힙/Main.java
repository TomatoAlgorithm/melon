package p_11286_절대값힙;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> plusPQ = new PriorityQueue<>();
        PriorityQueue<Integer> minusPQ = new PriorityQueue<>(Collections.reverseOrder());

        for(int i=0;i<n;i++){
            int x = Integer.parseInt(br.readLine());

            if(x == 0){
                if(plusPQ.size() == 0 && minusPQ.size() == 0){
                    System.out.println(0);
                }else if(plusPQ.size() == 0){
                    System.out.println(minusPQ.poll());
                }else if(minusPQ.size() == 0){
                    System.out.println(plusPQ.poll());
                }else{
                    int minus = minusPQ.peek();
                    int plus = plusPQ.peek();
                    if(Math.abs(minus) > plus){
                        System.out.println(plusPQ.poll());
                    }else{
                        System.out.println(minusPQ.poll());
                    }
                }
            }
            else{
                if(x>0){
                    plusPQ.add(x);
                }else{
                    minusPQ.add(x);
                }
            }
        }

    }
}
