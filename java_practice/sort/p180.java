package java_practice.sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class p180 {
    static int n;
    static List<Student> lst;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        lst = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine()," ");

            lst.add(new Student(st.nextToken(),Integer.parseInt(st.nextToken())));
        }

        Collections.sort(lst);
        for (int i = 0; i < n; i++) {
            System.out.print(lst.get(i).getName() + " ");
        }
    }

    static class Student implements Comparable<Student> {
        String name;
        int score;
        public Student(String name, int score) {
            this.name = name;
            this.score = score;
        }
        public String getName() {
            return name;
        }

        @Override
        public int compareTo(Student o) {
            return this.score - o.score;
        }
    }
}
