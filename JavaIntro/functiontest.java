public class functiontest{
	public static double average(int[] values){
		int total = 0;
		for (int v : values){
			total += v;
		}
		return (double) total/values.length;
	}


	public static void main(String[] args){

		int[] scores = {88, 92, 78, 95};

		double avg = average(scores);

		System.out.println("Average: " + avg);

	}

}
