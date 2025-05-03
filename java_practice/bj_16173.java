package java_practice;

import java.io.*;
import java.util.*;

public class bj_16173 {
    static int n;
    static ArrayList<ArrayList> lst = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            ArrayList row = new ArrayList();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {

                row.add(Integer.parseInt(st.nextToken()));
            }
            lst.add(row);
        }
        for (ArrayList arr : lst) {
            System.out.println(arr);

        }
    }
}
