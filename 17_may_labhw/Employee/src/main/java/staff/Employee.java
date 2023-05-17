package staff;

public abstract class Employee {

    private String name;
    private int niNumber;
    private double salary;

    public Employee(String name, int niNumber, double salary){
        this.name = name;
        this.niNumber = niNumber;
        this.salary = salary;
    }

    public String getName(){
        return this.name;
    }

    public int getNINumber(){
        return this.niNumber;
    }

    public double getSalary() {
        return this.salary;
    }

    public void raiseSalary(double raise){
        this.salary += raise;
    }

    public double payBonus(){
        return this.salary * 0.01;
    }
}
