package java_practice;

import java.io.*;
import java.util.*;

public class bj_16173 {
    static int n;
    static int[][] lst;
    static boolean[][] visited;
    static int gx,gy;
    static boolean dfs(int x,int y){
        visited[x][y] = true;

        int down_nx = x + lst[x][y];
        int down_ny = y;

        int right_nx = x;
        int right_ny = y + lst[x][y];
        if ( down_nx >=0 && down_nx < n && down_ny>=0 && down_ny < n && lst[down_nx][down_ny] == -1){
            return true;
        }
        if (right_nx >=0 && right_nx < n && right_ny>=0 && right_ny < n && lst[right_nx][right_ny] == -1){
            return true;
        }

        if (down_nx >=0 && down_nx < n && down_ny>=0 && down_ny < n && !visited[down_nx][down_ny]){
            return dfs(down_nx,down_ny);
        }
        if (right_nx >=0 && right_nx < n && right_ny>=0 && right_ny < n && !visited[right_nx][right_ny]){
            return dfs(right_nx,right_ny);
        }

        return false;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        lst = new int[n][n];
        gx = n;
        gy = n;
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {

                lst[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        boolean k = dfs(0,0);
        if (k==true){
            System.out.println("HaruHaru");
        }
        else{
            System.out.println("Hing");
        }
    }

}
