import java.io.IOException;
import java.util.HashMap;

public class Disguise {
    static class Solution {

        HashMap<String,Integer> map = new HashMap<>();
        static int answer = 0;

        public int solution(String[][] clothes) {
            // 데이터 삽입
            for (String[] clothe : clothes) {
                if (map.containsKey(clothe[1]))
                    map.put(clothe[1], map.get(clothe[1]) + 1);
                else
                    map.put(clothe[1], 1);
            }
            Object[] tmp = map.values().toArray();
            int[] values = new int[tmp.length];
            for (int i = 0; i < values.length; i++) {
                values[i] = (int) tmp[i];
            }
            comb(values,0,values.length,1);
            return answer;
        }
        void comb(int[] values,int start, int end, int before) {

            for (int k = start; k < end; k++) {
                answer += values[k] * before;
                comb(values, k + 1, end, values[k] * before);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        Solution s = new Solution();
        System.out.println(s.solution(new String[][] {{"y", "h"}, {"blue_sunglasses", "h"}, {"green_turban", "h"},{"y", "b"}, {"blue_sunglasses", "b"}, {"green_turban", "c"}}));

    }
}
