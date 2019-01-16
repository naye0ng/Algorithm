package algorithm;

import java.util.Scanner;

public class Baekjoon1783 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int w = sc.nextInt();
		if(h==1)System.out.println(1);
		else if(h==2) {
			System.out.println(Math.min(4,(w+1)/2));
		}
		else {
			if(w<7) {
				System.out.println(Math.min(4,w));
			}else {
				System.out.println(w-2);
			}
		}
	}

}
