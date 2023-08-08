package p_26042_식당입구대기줄;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Queue<Integer> line = new LinkedList<>();

        int maxLine = -1;
        int answerStudent = -1;
        int lastStudent = -1;

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");

            if (input[0].equals("1")) {
                int student = Integer.parseInt(input[1]);
                line.offer(student);
                lastStudent = student;
            } else if (input[0].equals("2")) {
                line.poll();
            }

            if (maxLine < line.size()) {
                maxLine = line.size();
                answerStudent = lastStudent;
            } else if (maxLine == line.size()) {
                if (lastStudent < answerStudent) answerStudent = lastStudent;
            }
        }

        System.out.println(String.format("%d %d", maxLine, answerStudent));
    }
}
