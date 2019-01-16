package algorithm;
import java.util.*;

public class Baekjoon1541 {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String input=sc.nextLine();
		
		String[] strArr = input.split("\\-");
		int ans=0;
		
		for(int i=0; i<strArr.length;i++) {
			String[] strArr2 = strArr[i].split("\\+");
			int tmp=0;
			for(String s:strArr2) {
				tmp+=Integer.parseInt(s);
			}
			if(i==0) {
				ans+=tmp;
				continue;
			}
			ans-=tmp;
		}
		System.out.println(ans);
	}
}
