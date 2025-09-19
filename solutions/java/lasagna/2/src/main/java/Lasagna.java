public class Lasagna {
    public int expectedMinutesInOven(){
        return 40;
    }
    public int remainingMinutesInOven(int timeSpent){
        Lasagna lasagna = new Lasagna();
        return lasagna.expectedMinutesInOven() - timeSpent;
    }
    public int preparationTimeInMinutes(int layers){
        return layers * 2;
    }
    public int totalTimeInMinutes(int layers, int timeSpent){
        Lasagna lasagna = new Lasagna();
        return lasagna.preparationTimeInMinutes(layers) + timeSpent;
    }
}
