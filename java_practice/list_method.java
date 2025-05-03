package Java;
import java.util.*;

public class list_method {

    public static void main(String[] args){
    // 1차원 배열
        int[] intList1 = new int[3];
        intList1[1] = 1;
        for (int i : intList1) {
            System.out.print(i);
        }
        // 1차원 배열 수정
        for (int i = 0 ; i < 3; i ++){
            intList1[i] = i;
        }
        for (int i : intList1) {
            System.out.print("i = " + i);
        }
        System.out.println();

        //1차원 배열 선언
        int[] intList3 = new int[] {1,2,3,4};
        for (int i : intList3) {
            System.out.print("i = " + i);
        }
        System.out.println();

        //2차원 배열 선언
        int[][] intList2 = new int[][]{{1,2,3,4},{5,6,7}};
        for (int[] ints : intList2) {
            System.out.println("ints = " + ints );
            for (int anInt : ints) {
                System.out.print("anInt = " + anInt + " ");
            }
            System.out.println();
            
        }
        System.out.println(intList2[1][2]);

        // 2차원 배열 선언
        int[][] intList9 = new int[3][3];
        for (int[] ints : intList9) {
            for (int anInt : ints) {
                System.out.print("anInt = " + anInt + " ");
            }
        }
        System.out.println();

        // ArrayList
        ArrayList<Integer> alst = new ArrayList<>();
        ArrayList alst2 = new ArrayList<>();
        //list 추가하기
        alst.add(1);

        System.out.println(alst);
        alst.add(2);
        System.out.println(alst);

        alst.add(Integer.parseInt("3"));
        System.out.println(alst);
        for (int i = 0; i <3 ; i++) {
            System.out.println(alst.get(i).getClass().getSimpleName());
        }

        //특정 위치 요소 삽입
        alst.add(1, 4);
//        alst.add(1, "one");
        System.out.println(alst);

        //리스트 합치기
        alst2.add(8);
        alst2.add(9);

        alst.addAll(alst2);

        System.out.println(alst);

        //리스트 요소 제거하기
        alst.remove(5);
        System.out.println(alst);

        // 배열 idx를 통해 얻기
        System.out.println(alst.get(4));

        // 특정 인덱스로 삭제하기
        System.out.println(alst.remove(3));
        //특정 값으로 삭제하기
        System.out.println(alst.remove("one"));
        // 특정 값(int) 로 삭제하기
        System.out.println(alst.remove(Integer.valueOf(3)));

        System.out.println(alst);

        alst.removeAll(alst2);
        System.out.println(alst);

        alst.addAll(alst2);
        System.out.println(alst);

        alst.retainAll(alst2);
        System.out.println(alst);

        //사이즈
        System.out.println(alst.size());
        int a = intList1.length;
        System.out.println(a);

        System.out.println(alst);
        System.out.println(alst2);
        boolean kk = alst.containsAll(alst2);

        System.out.println(kk);
        System.out.println(alst);
        for (int i = 0; i <4 ; i++) {
            alst.add(i);
        }
        System.out.println(alst);
        alst.removeIf(x -> (x % 2) == 0);

        for (Object o : alst) {
            System.out.println(o.getClass().getSimpleName());
        }

        System.out.println(alst);
        }




}
