class Student{
	private String name;
	private int[] scores;

	public Student(String name, int[] scores){
		this.name = name;
		this.scores = scores;
	}

	public double average(){
		int total = 0;
		for (int s : scores) {
			total += s;
		}
		return (double) total / scores.length;
	}
	public static void main(String[] args){
		Student nik = new Student("Nikolas", new int[]{88,92,79});
		System.out.println(nik.name);
	}
}

