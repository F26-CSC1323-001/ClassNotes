public class scorestest{

	public static void main(String[] args){
		int[] scores = {88, 92, 78, 95};
		int total = 0;
		for (int i = 0; i < scores.length; i++){
			total += scores[i];
		}
		double avg = (double) total / scores.length;
		System.out.println("Average: " + avg);

		String name = "Nikolas";
		System.out.println("Name Length: " + name.length());

	}
}
