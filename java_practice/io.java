import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class io {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            
        }

        for (int i : arr) {
            System.out.println("i = " + i);
        }

    }
}
