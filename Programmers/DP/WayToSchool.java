public class WayToSchool {
    static class Solution {
        public int solution(int m, int n, int[][] puddles) {
            int[][] map = new int[n][m];
            for (int[] puddle : puddles) {
                map[puddle[1]-1][puddle[0]-1] = -1;
            }

            // 초기화
            int value = 1;
            for (int x = 0; x < n; x++) {
                if (map[x][0] == -1)
                    value = 0;
                map[x][0] = value;
            }
            value = 1;
            for (int y = 0; y < m; y++) {
                if (map[0][y] == -1)
                    value = 0;
                map[0][y] = value;
            }

            for (int x = 1; x < n; x++) {
                for (int y = 1; y < m; y++) {
                    if (map[x][y] == -1)
                        map[x][y] = 0;
                    else {
                        map[x][y] = (map[x - 1][y] + map[x][y - 1])% 1000000007;
                    }
                }
            }
            return map[n - 1][m - 1];
        }
    }
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        System.out.println(s.solution(100, 100, new int[][]{}));
    }
}
