import java.util.Scanner;

/**
 * Problem:
 * https://www.hackerrank.com/challenges/stepping-stones-game
 *
*/

public class Solution {

	public static void main(String[] args) {
	
		// Fetch the STDIN input
		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
	
		long[] cs = new long[t];
		for(int i = 0; i < t; i++)
			cs[i] = scanner.nextLong();
	
		for(int i = 0; i < cs.length; i++)
			steppingStone(cs[i]);
	}
	
	public static void steppingStone(long c) {
		
		/**
		 * Basic algebra:
		 * 
		 * 	c = n * (n+1) * 0.5
		 * 
		 *  Solve for n, using quadratic formula.
		 *  
		 *  We take the positive answer and check if it's an integer.
		 */
	
		// 2 possible answers
		double n1 = (-1 + Math.sqrt(8 * c + 1)) / 2;
		double n2 = (-1 - Math.sqrt(8 * c + 1)) / 2;
	
		// takes the positive answer
		double answer = n1 >= 0 ? n1 : n2;
	
		// Check if the answer is an integer.
		String message = Math.floor(answer) == Math.ceil(answer) ? "Go On Bob " + (int)answer : "Better Luck Next Time";
		System.out.println(message);
	}
}
