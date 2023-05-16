public class WaterBottle {
    private int volume;

    public WaterBottle(){
        this.volume = 100;
    }

    public int getVolume(){
        return this.volume;
    }

    public void setVolume(int newVolume){
        this.volume = newVolume;
    }

    public int drink(){
        if (this.volume >= 10){
        int newVolume = this.volume - 10;
        setVolume(newVolume);
        return this.volume;}
        return this.volume;
    }

    public void empty(){
        setVolume(0);
    }

    public void fill(){
        setVolume(100);
    }
}
