public class Printer {
    private int paper;
    private int toner;

    public Printer(int paper, int toner){
        this.paper = paper;
        this.toner = toner;
    }

    public int getPaperInPrinter(){
        return this.paper;
    }

    public void setPaperInPrinter(int newPages){
        this.paper = newPages;
    }

    public void print(int pages, int copies){
        int pagesPrinted = pages * copies;
        if (this.paper >= pagesPrinted && this.toner >= pagesPrinted) {
            int newPages = this.paper - pagesPrinted;
            setPaperInPrinter(newPages);
            int newToner = this.toner - pagesPrinted;
            setToner(newToner);
        }
    }

    public int getToner(){
        return this.toner;
    }

    public void setToner(int newToner){
        this.toner = newToner;
    }
}
