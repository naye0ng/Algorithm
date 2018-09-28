package algorithm;

import java.util.Scanner;

public class Baekjoon11048 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        //자바는 자동으로 배열을 0으로 초기화 
        int[][] a = new int[n+1][m+1];
        int[][] d = new int[n+1][m+1];
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                a[i][j]=in.nextInt();
            }
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                d[i][j]=Math.max(d[i-1][j],d[i][j-1])+a[i][j];
            }
        }
        System.out.println(d[n][m]);
	}

}
