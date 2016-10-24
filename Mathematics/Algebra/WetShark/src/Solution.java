/**
 * Problem:
 * https://www.hackerrank.com/challenges/wet-shark-and-42
 */

import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int t = scanner.nextInt();
		long[] strengths = new long[t];
		
		for(int i = 0; i < t; i++)
			strengths[i] = scanner.nextLong();
		
		for(int i = 0; i < t; i++)
			wetShark(strengths[i]);
	}
	

	/**
	 * Calculate the square where the WetShark will stop based on its initial strength.
	 * 
	 * Condition to lose strength:
	 * (square % 2 || square % 4) && !(square % 42)
	 * 	
	 * Since 2|4, we can just count the square that are divisble by 2.
	 * So, the strength * 2 will give us the number (n) of square needed to put that beast to 0 strength.
	 * Finally, we need to substract to this number n = n - (n / 42).
	 * 	
	 * @param s Strength value.
	 */
	private static void wetShark(long s){
		long n = s % 2 == 0 ? s * 2 : (s * 2);
		System.out.println(n + (n / 42));
	}

}