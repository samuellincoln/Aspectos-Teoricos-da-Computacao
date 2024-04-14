import java.util.ArrayList;
import java.util.List;
public class SubsetSum {
	public static int sum (List <Integer> subset) {
		int s = 0;
		for (Integer v : subset) {
			s += v;
		}
		return s;
	}
	public static boolean verify (List <Integer> set, List <Integer> subsettarget, int value) {
		return set.containsAll (subsettarget) && sum (subsettarget) == value;
	}
	public static ArrayList <Integer> sums (List <Integer> set) {
		ArrayList <Integer> currentsums = new ArrayList <Integer> ();
		for (Integer v : set) {
			ArrayList <Integer> crrsumaux = new ArrayList <Integer> ();
			currentsums.forEach(e -> crrsumaux.add (e + v));
			currentsums.addAll(crrsumaux);
			currentsums.add(v);
		}
		return currentsums;
	}
	public static boolean decide (List <Integer> set, int value) {
		return sums (set).contains (value);
	}
	public static void main (String [] args) {
		List <Integer> set = List.of (4, 11, 16, 21, 27);
		List <Integer> subset = List.of (0, 5, 3, 7);
		int value = 25;
		boolean verification = verify (set, subset, value);
		System.out.println (decide (set, 25));
	}
}
