package p_16946_벽부수고이동하기4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Failed {
    static int N, M;
    static int[][] map, outMap;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        outMap = new int[N][M];
        ArrayList<int[]> wallList = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == '1') {
                    map[i][j] = 1;
                    wallList.add(new int[]{i, j});
                }
            }
        }

        for (int[] point :
                wallList) {
            int cnt = canMoveCnt(point);
            outMap[point[0]][point[1]] = cnt;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(outMap[i][j]);
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    private static int canMoveCnt(int[] point) {
        Queue<int[]> queue = new LinkedList();
        boolean[][] visited = new boolean[N][M];
        int[] startPoint = {point[0], point[1]};

        queue.add(startPoint);
        int cnt = 0;

        while (queue.size() != 0) {
            int[] cur = queue.poll();
            cnt++;

            for (int i = 0; i < 4; i++) {
                int wy = cur[0] + dy[i];
                int wx = cur[1] + dx[i];

                if(wy >= 0 && wy < N && wx >=0 && wx<M && !visited[wy][wx] && map[wy][wx] == 0){
                    queue.offer(new int[]{wy, wx});
                    visited[wy][wx] = true;
                }
            }
        }

        return cnt;
    }


}
