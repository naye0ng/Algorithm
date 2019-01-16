package algorithm;
import java.util.*;

public class Baekjoon1744 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int zero=0, one =0;
		
		ArrayList<Integer> plus = new ArrayList<>();
		ArrayList<Integer> minus = new ArrayList<>();

		for(int i=0; i<n; i++) {
			int num = sc.nextInt();
			if(num<0) minus.add(num);
			else if(num==0) zero++;
			else if(num==1) one++;
			else plus.add(num);	
		}
		
		Collections.sort(plus);
		Collections.sort(minus);
		Collections.reverse(plus);
		
		if(minus.size()%2==1) {
			minus.add(zero>0?0:1);//1넣으면 그냥 그 수임 
		}
		if(plus.size()%2==1) {
			plus.add(1);//1넣어서 짝수 맞춰주자 
		}
		
		int ans=0;
		
		for(int i=0; i<plus.size();i+=2) {
			ans+=plus.get(i)*plus.get(i+1);
		}
		for(int i=0; i<minus.size();i+=2) {
			ans+=minus.get(i)*minus.get(i+1);
		}
		
		System.out.println(ans+one);
		//System.out.println(plus);
		//System.out.println(minus);
		
	}

}
