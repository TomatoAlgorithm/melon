package p_15649_N과M;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");

        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[1]);

        dfs(0, new int[m], n);

        for (int[] arr :
                AL) {
            for(int i : arr){
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }


    static ArrayList<int[]> AL = new ArrayList<>();


    public static void dfs(int depth, int[] arr, int max) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i=0;i < depth;i++){
           if(set.contains(arr[i])) return;
           set.add(arr[i]);
        }
        if (depth == arr.length) {
            AL.add(arr);
            return;
        }

        for (int i = 1; i <= max; i++) {
            arr[depth] = i;
            dfs(depth + 1, arr.clone(), max);
        }
    }
}
