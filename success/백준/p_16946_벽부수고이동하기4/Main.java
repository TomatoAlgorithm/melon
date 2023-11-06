package p_16946_벽부수고이동하기4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] map, outMap;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        outMap = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == '1') {
                    map[i][j] = -1;
                    outMap[i][j] = 1;
                }
            }
        }

        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if(map[i][j] == 0 && !visited[i][j]){
                    setOutMap(new myPoint(i,j));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(outMap[i][j]%10);
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    private static void setOutMap(myPoint startPoint) {
        Queue<myPoint> queue = new LinkedList();
//        Set<myPoint> area = new HashSet<>(); //이 구역에 대해서 값을 업데이트하면 시간초과가 나옴 -> visited로 판별하게 변경 후 성공
        Set<myPoint> meetList = new HashSet<>();

//        area.add(startPoint);
        queue.add(startPoint);
        visited[startPoint.y][startPoint.x] = true;
        int cnt = 0;

        while (queue.size() != 0) {
            myPoint cur = queue.poll();
//            area.add(cur);
            cnt++;

            for (int i = 0; i < 4; i++) {
                int wy = cur.y + dy[i];
                int wx = cur.x + dx[i];

                if(wy >= 0 && wy < N && wx >=0 && wx<M && !visited[wy][wx]){
                    if(map[wy][wx] == 0){
                        queue.offer(new myPoint(wy, wx));
                        visited[wy][wx] = true;
                    }else if(map[wy][wx] == -1){
                        meetList.add(new myPoint(wy, wx));
                    }
                }
            }
        }

//        for(myPoint arr : area){
//            map[arr.y][arr.x] = cnt;
//        }
        for(myPoint arr : meetList){
            outMap[arr.y][arr.x]+=cnt;
        }
    }


}
class myPoint{
    public int y;
    public int x;

    public myPoint(int y, int x) {
        this.y = y;
        this.x = x;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        myPoint myPoint = (myPoint) o;
        return y == myPoint.y && x == myPoint.x;
    }

    @Override
    public int hashCode() {
        return Objects.hash(y, x);
    }
}