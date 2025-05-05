package java_practice.sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class p178 {
    static int n;
    static ArrayList lst;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        lst = new ArrayList(){};
        for (int i = 0; i < n; i++) {
            lst.add(br.readLine());
        }
        Collections.sort(lst);
        System.out.println(lst);

        Collections.sort(lst, Collections.reverseOrder());
        System.out.println(lst);
        for (Object o : lst) {
            System.out.print(o + " ");
        }
    }
}
