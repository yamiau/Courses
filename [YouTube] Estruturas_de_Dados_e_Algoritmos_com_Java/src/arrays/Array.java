package arrays;

public class Array {
	private String[] elements;
	private int length;
	
	public Array(int length) {
		this.elements = new String[length];
	}
	
	
//	public void add(String element) {
//		for (String i : elements) {
//			if (i == null) {
//				i = element;
//				break;
//			}
//		}
//	}
	
	public boolean add(String element) {
		
		if (this.length < this.elements.length) {
			this.elements[this.length] = element;
			this.length++;
			return true;
		} 
		return false;			
	}
}
