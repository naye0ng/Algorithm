package algorithm;

import java.util.Scanner;

public class Beakjoon2875 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int w = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		int n=0, ans=0; //나머지 
		
		if(m*2==w) ans=m;
		else if(m*2>w) {ans=w/2; n=m-ans;}
		else if(m*2<w) {ans=m; n=w-m*2;}

		if(k>n) {
			ans-=((k-n)%3==0 ? (k-n)/3:(k-n)/3+1);
		}
		System.out.println(ans);
	}

}
