package java_practice;

public class quick_sort {
    static int[] lst = new int[]{2,4,5,3,1,0,7,9,8,6};

    public static void main(String[] args){
        quick_sort(lst,0,9);
        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
        }


    }
    static void quick_sort(int[] lst, int s, int e){
        if (s >= e){
            return;
        }
        int p = s;
        int l = s + 1;
        int r = e;

        while(l <r){
            while (l <= e && lst[l] <= lst[p]){
                l += 1;
            }
            while (r > s && lst[r] >= lst[p]){
                r -= 1;
            }
            if (l > r) {
                int v =  lst[p];
                lst[p] = lst[r];
                lst[r] = v;
            }
            else{
                int t1 = lst[l];
                lst[l] = lst[r];
                lst[r] = t1;
            }
            quick_sort(lst,s,r-1);
            quick_sort(lst,r+1,e);
        }
    }
}
