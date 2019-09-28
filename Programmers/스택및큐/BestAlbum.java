import java.util.*;

public class BestAlbum {
    static  class Solution {
        public class Genre{
            int total = 0;
            ArrayList<int[]> music = new ArrayList<>();

            public Genre(int index, int plays) {
                this.total += plays;
                this.music.add(new int[]{index, plays});
            }

        }

        public int[] solution(String[] genres, int[] plays) {
            HashMap<String, Genre> map = new HashMap<>();
            for(int i =0; i< genres.length;i++){
                if(map.containsKey(genres[i])){
                    // 이미 존재하면, 이전 객체 넣고
                    map.put(genres[i], map.get(genres[i]));
                    // 값 추가
                    map.get(genres[i]).music.add(new int[]{i, plays[i]});
                    map.get(genres[i]).total += plays[i];
                }else {
                    map.put(genres[i], new Genre(i, plays[i]));
                }
            }

            ArrayList<Integer> answer = new ArrayList<>();

            // Value 기준으로 정렬된 iterator기준으로 빼내기
            Iterator it = sortByValue(map).iterator();
            while(it.hasNext()){
                ArrayList<int[]> arr = map.get(it.next()).music;
                //내부 오름차순 정렬하기
                arr.sort(new Comparator<int[]>() {
                    @Override
                    public int compare(int[] o1, int[] o2) {
                        return o2[1]-o1[1];
                    }
                });
                // 앞에서 최대 두 개씩만 꺼내기
                int i = 0;
                for(int[] index: arr){
                    if(i>=2) break;
                    answer.add(index[0]);
                    i++;
                }
            }
            int[] intAnswer = new int[answer.size()];
            int size = 0;
            for(int a : answer){
                intAnswer[size++] = a;
            }
            return intAnswer;
        }

        // https://jobc.tistory.com/176
        // value 기준으로 hashmap 내림차순 정렬하기
        public List sortByValue(Map map){
            // key 배열 생성
            List<String> keys = new ArrayList<>(map.keySet());
            //keys.addAll(map.keySet());

            // key 배열을 value 값 순으로 정렬
            Collections.sort(keys, new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    Genre g1 = (Genre)map.get(o1);
                    Genre g2 = (Genre) map.get(o2);
                    return g2.total-g1.total;
                }
            });

            return keys;
        }
    }

    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 500, 800,2500})));
    }
}