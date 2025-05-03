

import java.util.*;
public class DFS{

    static ArrayList<ArrayList<Integer>> G = new ArrayList<>();
    static boolean[] visited;
    public static void main(String[] args){
        int n = 5;
        int v = 1;
        visited = new boolean[n+1];

        for (int i = 0; i< n +1; i ++){
            G.add(new ArrayList<>());
        }


        addEdge(1,2);
        addEdge(1,3);
        addEdge(2,4);
        addEdge(3,5);

        dfs(1);
    }

    static void addEdge(int v, int k) {
        G.get(v).add(k);
        G.get(k).add(v);
    }
    static void dfs(int node){

        visited[node] = true;
        System.out.println("visited " + node);

        for(int next: G.get(node)){
            if (!visited[next]){
                dfs(next);
            }
        }
    }
}