import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

public class NoodlesFactory {
    static class Solution {
//        class Supply implements Comparable<Supply>{
//            int date;
//            int supply;
//
//            public Supply(int date, int supply) {
//                this.date = date;
//                this.supply = supply;
//            }
//
//            @Override
//            public int compareTo(Supply o) {
//                // 내림차순 정렬
//                return o.supply-this.supply;
//            }
//        }
//        class Supply {
//            int date;
//            int supply;
//
//            public Supply(int date, int supply) {
//                this.date = date;
//                this.supply = supply;
//            }
//        }
        public int solution(int stock, int[] dates, int[] supplies, int k) {
            // 변환환

            ArrayList<Integer> arrDates = new ArrayList<>();
            for(int date : dates){
                arrDates.add(Integer.valueOf(date));
            }
            ArrayList<Integer> arrSupplies = new ArrayList<>();
            for(int supply : supplies){
                arrSupplies.add(Integer.valueOf(supply));
            }

            PriorityQueue<Integer> que = new PriorityQueue<>(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1,Integer o2) {
                    return o2-o1;
                }
            });

            int answer = 0;
            while (stock < k){
                int I = 0;
                for(int i=I ; i < arrDates.size(); i++){
                    if(arrDates.get(i) <= stock){
                        que.offer(arrSupplies.get(i));
                        I++;
                    }else{
                        break;
                    }
                }
                // 삭제
                for(int i=I-1; i>=0; i--){
                    arrDates.remove(i);
                    arrSupplies.remove(i);
                }
                stock += que.poll();

                answer += 1;
            }

            return answer;
        }
    }
    public static void main(String[] args) throws IOException {
        Solution s = new Solution();
        System.out.println(s.solution(10,new int[]{5,10},new int[]{1,100},100));

    }
}