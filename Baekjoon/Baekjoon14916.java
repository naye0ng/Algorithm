package algorithm;

import java.util.Scanner;

public class Baekjoon14916 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int i = in.nextInt();
		int count=0;
		if(i<5 && i%2!=0) {count=-1;}
		else if(i%5==0) {count=i/5;}
		else {
			i=i-2;
			count++;
			while(i%5!=0) {
				count++;
				i-=2;
				if(i%5==0) {
					count+=i/5; i=-1; break;}
			}
			count = i==-1? count : count+i/5;
		}
		
		System.out.println(count);
		
	}


}
