package p_2615_오목;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int BOARD_SIZE = 19;
    static int[][] board = new int[BOARD_SIZE][BOARD_SIZE];
    static boolean[][] visited = new boolean[BOARD_SIZE][BOARD_SIZE];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < BOARD_SIZE; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < BOARD_SIZE; j++) {
                board[i][j] = Integer.parseInt(line[j]);
            }
        }

        int[] dx = {1, 0, 1, 1};
        int[] dy = {0, 1, 1, -1};

        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                if (board[i][j] != 0) {
                    int color = board[i][j];
                    for (int k = 0; k < dx.length; k++) {
                        int[] cnt = solution(color, i, j, dx[k], dy[k]);
                        if (cnt[0] == 5) {
                            printResult(color, cnt[1], cnt[2]);
                            return;
                        }
//                        if (dfs(color, 1, i, j, dx[k], dy[k])) {
//                            if (!isOverSix(color, i, j, dx[k], dy[k])) {
//                                printResult(color, i, j);
//                                return;
//                            }
//                        }
                    }
                }
            }
        }

        System.out.println(0);
    }

//    private static boolean dfs(int color, int depth, int y, int x, int dx, int dy) {
//        if (depth == 5) {
//            return true;
//        }
//
//        int wy = y + dy;
//        int wx = x + dx;
//
//        if (wy >= 0 && wy < BOARD_SIZE && wx >= 0 && wx < BOARD_SIZE && board[wy][wx] == color) {
//            return dfs(color, depth + 1, wy, wx, dx, dy);
//        }
//
//        return false;
//    }

    private static int[] solution(int color, int y, int x, int dx, int dy) {
        int[] res = new int[]{1, y, x};

        int ny = y + dy;
        int nx = x + dx;

        while (ny >= 0 && ny < BOARD_SIZE && nx >= 0 && nx < BOARD_SIZE && board[ny][nx] == color) {
            res[0]++;

            if(res[2] > nx ){
                res[2] = nx;
                res[1] = ny;
            } else if (res[2] == nx) {
                if(res[1] >ny){
                    res[2] = nx;
                    res[1] = ny;
                }
            }

            ny += dy;
            nx += dx;
        }

        ny = y - dy;
        nx = x - dx;

        while (ny >= 0 && ny < BOARD_SIZE && nx >= 0 && nx < BOARD_SIZE && board[ny][nx] == color) {
            res[0]++;

            if(res[2] < nx ){
                res[2] = nx;
                res[1] = ny;
            } else if (res[2] == nx) {
                if(res[1] <ny){
                    res[2] = nx;
                    res[1] = ny;
                }
            }

            ny -= dy;
            nx -= dx;
        }

        return res;
    }

    private static void printResult(int color, int y, int x) {
        System.out.println(color);
        System.out.println((y + 1) + " " + (x + 1));
    }
}
