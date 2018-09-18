package algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Baekjoon10610 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
        char[] s = sc.nextLine().toCharArray();
        int sum = 0, mul=1;
        for (int i=0; i<s.length; i++) {
            sum += s[i] - '0';
            mul *= s[i] - '0'; //이부분만 바꼈는데 왜 출력초과가 나는가? 
        }
        Arrays.sort(s);
        System.out.println(mul);
        if (mul == 0 && sum%3 == 0) {
            for (int i=s.length-1; i>=0; i--) {
                System.out.print(s[i]);
            }
            System.out.println();
        } else {
            System.out.println(-1);
        }
		/*
		Scanner sc =new Scanner(System.in);
		char[] input = sc.nextLine().toCharArray();
		int check = 0, check2=1; //합, 곱을 체크 
		
		for(int i=0;i<input.length;i++) {
			check +=(input[i]-'0');
			check2 *=input[i]-'0';
		}
		System.out.print(check2);
		if(check%3==0 && check2==0) {//합이 3의 배수 이면서 곱이 0이면 
			Arrays.sort(input);
			String ans="";
			
			for(int i=input.length-1;i>=0;i--) {
				ans+=(input[i]-'0');
			}
			System.out.print(ans);
			
		}else System.out.println(-1);
		*/
	}

}
