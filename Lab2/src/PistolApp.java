/**
 * lab 2 package
 */
package KI306.Fodor.Lab2;
import java.io.*;

/**
 * Pistol Application class implements main method for
 * Pistol class abilities demonstration
 */
public class PistolApp {

    /**
     * @param args
     * @throws FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        Pistol p1 = new Pistol();
        Pistol p2 = new Pistol();
        Pistol p3 = new Pistol();
        Pistol pp1 = new Pistol(3, "Model1");
        Pistol pp2 = new Pistol(9, "Model2");

        //Representation
        System.out.println("Model of your pistol is "+ p1.getGunsModel());
        System.out.println("Now you have "+ p1.getGunsBulletCount() + " bullets");
        //Make 7 shoots at distance 10 m.
        System.out.println("-----Start shooting------");
        p1.makeSomeShoots(15, 20);
        //Statistics
        System.out.println("Your accuracy is " + p1.getAccuracy());
        System.out.println("You have " + p1.getHitShoots() + " hit shoots");
        System.out.println("You have " + p1.getMissedShoots() + " missed shoots");
        System.out.println("Your pistol serviceability is  " + p1.getGunsServiceability());
        System.out.println("Now you have "+ p1.getGunsBulletCount() + " bullets");
        //Pistol reloading
        p1.reloadGun();
        System.out.println("-----Reloaded pistol-----");
        System.out.println("Now you have "+ p1.getGunsBulletCount() + " bullets");
        //Pistol repairing
        p1.RepairGun(500);
        System.out.println("Your pistol serviceability is  " + p1.getGunsServiceability());

        System.out.println("Without parameters = " + Pistol.countWithoutParam +
                "\nWith parameters = " + Pistol.countWithParam);
        p1.dispose();
    }
}
