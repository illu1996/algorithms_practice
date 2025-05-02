import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] lst = new int[n];

        for (int i = 0 ; i < n; i ++){
            lst[i] = sc.nextInt();
        }
        int v = sc.nextInt();

        int cnt = 0;

        for (int k: lst){
            if (k== v){
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}