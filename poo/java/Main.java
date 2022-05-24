class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberx = new UberX("AMQ123",new Account("Andres Herrera","AND123","",""),"Chevrolet","Sonic");
        uberx.setPassenger( 4);
        uberx.printDataCar();

        /*Car car2 = new Car("QWE567",new Account("Andrea Herrera","ANDA876","",""));
        car2.passegenger = 3;
        car2.printDataCar();*/


    }
}