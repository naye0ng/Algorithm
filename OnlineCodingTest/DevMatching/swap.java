import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int numbers[] = { 10, 40, 30, 20};
		int K = 20;

		System.out.println(solution(numbers, K));

	}
	public static boolean init(int numbers[], int K) {
		int numbers2[] = new int[numbers.length];
		for(int i=0;i<numbers.length;i++) {
			numbers2[i] = numbers[i];
		}
		Arrays.sort(numbers2);
		
		for(int i=0;i<numbers.length-1;i++) {
			if(Math.abs(numbers2[i]-numbers2[i+1])>K)return false;
		}
		return true;
	}

	public static int fac(int n) {
		if (n == 1)
			return 1;
		return fac(n - 1) * n;
	}

	public static int solution(int[] numbers, int K) {
		int answer = Integer.MAX_VALUE;
		int start = 0;
		int end = fac(numbers.length);

		if(!init(numbers, K))
			return -1;
		
		while (start <= end) {
			flag = false;
			solve2(start, numbers, K);
			if (flag == true) {
				return start;
			}
			start++;
		}
		/* (start <= end) {
			int mid = start + end;
			flag = false;
			solve2(mid, numbers, K);
			if (flag == true) {
				end = mid;
				answer = Math.min(answer, mid);
			} else {
				start = mid + 1;
			}
		}*/
		if (flag)
			return (start);
		else
			return -1;
	}

	public static boolean flag;

	public static void solve2(int n, int numbers[], int k) {
		if (n <= 0) {
			if (check(numbers, k)) {
				flag = true;
			}
			return;
		}
		int n1 = numbers.length;
		for (int i = 0; i < n1; i++) {
			for (int j = i + 1; j < n1; j++) {
				swap(i, j, numbers);
				solve2(n - 1, numbers, k);
				swap(i, j, numbers);
			}
		}

	}

	public static void swap(int a, int b, int numbers[]) {
		int tmp = numbers[b];
		numbers[b] = numbers[a];
		numbers[a] = tmp;

	}

	public static boolean check(int numbers[], int k) {
		for (int i = 0; i < numbers.length - 1; i++) {
			if (Math.abs(numbers[i] - numbers[i + 1]) <= k) {
				continue;
			} else
				return false;
		}
		return true;
	}

}