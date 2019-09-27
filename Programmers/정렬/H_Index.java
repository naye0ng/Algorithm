import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

public class H_Index {
    static class Solution {
        public int solution(int[] citations) {
            ArrayList<Integer> arr = new ArrayList<>();
            for(int c : citations){
                arr.add(c);
            }
            arr.sort(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    // 오름차순으로 정렬 앞 < 뒤 이면 바꾸기
                    return o2-o1;
                }
            });
            int answer = 0;
            for(int h = arr.size();h >=0; h--){
                int upper= 0, lower = 0;

                for(int x=0;x<arr.size();x++){
                    if(arr.get(x) >= h)
                        upper ++;
                    else
                        lower++;
                }
                if(upper >= h && lower <= h) {
                    answer = h;
                    break;
                }
            }
            return answer;
        }
    }
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t=0;t<T;t++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] arr = new int[st.countTokens()];
            int i = 0;
            while(st.hasMoreTokens()){
                arr[i++] = Integer.parseInt(st.nextToken());
            }
            System.out.println(s.solution(arr));
        }
    }
}

/*
1
3 0 6 1 5
 */