import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Network {
    static class Solution {
        Queue<Integer> que = new LinkedList<>();

        public int solution(int n, int[][] computers) {
            int answer=0;
            boolean[] visited = new boolean[n];
            Arrays.fill(visited,false);
            for(int i=0;i<n;i++){
                if(!visited[i]){
                    visited[i] = true;
                    answer++;
                    que.add(i);
                    int q;
                    while(!que.isEmpty()){
                        q = que.poll();
                        for(int j=0;j<n;j++){
                            if(!visited[j] && computers[q][j]== 1){
                                visited[j] = true;
                                que.add(j);
                            }
                        }

                    }
                }
            }

            return answer;
        }
    }
    public static void main(String[] args) throws IOException {
        Solution s = new Solution();
        System.out.println(s.solution(3,new int[][] {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}}));
    }
}
