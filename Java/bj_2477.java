
import java.lang.reflect.Array;
import java.util.*;

public class bj_2477 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int cnt_ = sc.nextInt();

        ArrayList<Integer> widths = new ArrayList<>();
        ArrayList<Integer> heights = new ArrayList<>();

        for (int i = 0; i < 6; i++)
        {
            int dir = sc.nextInt();
            if (dir == 1 || dir == 2){
                widths.add(sc.nextInt());
            }
            else{
                heights.add(sc.nextInt());
            }
        }

        // 최대 가로 세로 변 곱해서 최소 가로 세로 변 빼기
        int max_width = Collections.max(widths);
        int max_height = Collections.max(heights);

        int max_l = max_height * max_width;
        System.out.println(widths);
        System.out.println(heights);
        int maxWIndex = widths.indexOf(max_width);
        int maxHIndex = heights.indexOf(max_height);

        int minusH = 0;
        int minusW = 0;
        if (maxWIndex == 0){
            minusH = Math.abs(heights.get(1) - heights.get(2));
        }
        else if (maxWIndex == 1){
            minusH = Math.abs(heights.get(0) - heights.get(2));
        }
        else if (maxWIndex == 2){
            minusH = Math.abs(heights.get(0) - heights.get(1));
        }

        if (maxHIndex == 0){
            minusW = Math.abs(widths.get(1) - widths.get(2));
        }
        else if (maxHIndex == 1){
            minusW = Math.abs(widths.get(0) - widths.get(2));
        }
        else if (maxHIndex == 2){
            minusW = Math.abs(widths.get(0) - widths.get(1));
        }
        System.out.println(minusH);
        System.out.println(minusW);
        int real_l = max_l - (minusW * minusH);
        System.out.println(real_l);

    }
}
