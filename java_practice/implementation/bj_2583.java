package java_practice.implementation;

import java.util.*;
import java.io.*;

public class bj_2583 {
    static int n,m,k;
    static int x1,y1,x2,y2;
    static int[][] map;
    //m 이 행이고, x가 행이다
    static boolean[][] visited;
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,1,0,-1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        //모눈종이 만들기
        map = new int[m][n];
        visited = new boolean[m][n];
        //직사각형 그리기
        for (int i = 0; i < k; i++) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            x1 = arr[0]; y1 = arr[1]; x2 = arr[2]; y2 = arr[3];
            draw(x1, y1, x2, y2);
        }
        int total = 0;
        ArrayList extent = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && map[i][j] == 0){
                    int kkk = bfs(i,j);
                    if (kkk != 0){
                        total++;
                        extent.add(kkk);
                    }
                }

            }

        }
        Collections.sort(extent);
        System.out.println(total);
        for (Object o : extent) {
            System.out.print(o+" ");
        }

    }
    static void draw(int x1,int y1,int x2,int y2){
        for (int i = x1; i <x2 ; i++) {
            for (int j = y1; j <y2 ; j++) {
                map[i][j] = 1;
            }
        }
    }
    static int bfs(int x, int y){
        int cnt =1;

        visited[x][y] = true;


        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x,y});

        while(!q.isEmpty()){
            int[] arr = q.poll();
            x = arr[0];
            y = arr[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && map[nx][ny] == 0){
                    visited[nx][ny] = true;
                    cnt++;
                    q.add(new int[]{nx,ny});
                }
            }
        }

        return cnt;
    }



}
