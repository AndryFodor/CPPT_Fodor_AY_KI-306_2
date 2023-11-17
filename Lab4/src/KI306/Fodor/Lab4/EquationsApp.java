package KI306.Fodor.Lab4;

import java.util.Scanner;
import java.io.*;
import static java.lang.System.out;
/**
 * Class <code>EquationsApp</code> Implements driver for Equations class
 */
public class EquationsApp {
    /**
     * @param args
     */
    public static void main(String[] args) {
        try {
            out.print("Enter file name: ");
            Scanner in = new Scanner(System.in);
            String fName = in.nextLine();
            PrintWriter fout = new PrintWriter(new File(fName));
            fout.println("sin(3x-5)/ctg(2x)");
            try {
                try {
                    Equations eq = new Equations();
                    out.print("Enter X: ");
                    int x = in.nextInt();
                    fout.println("for value of x = " + x + "° is equal ");
                    fout.print(eq.calculate(x));
                    out.print("Result is " + eq.calculate(x));
                }
                finally {
                    fout.flush();
                    fout.close();
                }
            }
            catch (CalcException | DividingByZeroException ex) {
                out.print(ex.getMessage());
            }
        }
        catch (FileNotFoundException ex) {
            out.print("Exception reason: Perhaps wrong file path");
        }
    }
}

/**
 * Class <code>CalcException</code> more precises ArithmeticException
 */
class CalcException extends ArithmeticException {
//    public CalcException(){}
    public CalcException(String cause) {
        super(cause);
    }
}

class DividingByZeroException extends ArithmeticException {
    DividingByZeroException(String cause){
        super(cause);
    }


}
/**
 * Class <code>Equations</code> implements method for y=sin(3x-5)/ctg(2x)expression * calculation
 */
class Equations {
    /**
     * Method calculates the y=sin(3x-5)/ctg(2x) expression
     * @param <code>x</code> Angle in degrees
     * @throws CalcException
     */
    public double calculate(int x) throws CalcException {
        double y, rad;
        rad = x * Math.PI / 180.0;
        try {
            y = 1/Math.tan(2*rad); // ctg(2x)
            y = Math.sin(3*rad-5)/y;
            if (y==Double.NaN || y==Double.NEGATIVE_INFINITY || y==Double.POSITIVE_INFINITY ||  x== 90)
                throw new CalcException("");
            else if(x==0)
                throw new DividingByZeroException("");
        }
        catch (CalcException | DividingByZeroException ex)
        {

            if (rad==Math.PI/2.0)
                throw new CalcException("Exception reason: Illegal value of X for cotangent calculation");
            else if (Math.tan(2*rad) == 0.0)
                throw new DividingByZeroException("Exception reason: Division by zero");
            else
                throw new CalcException("Unknown reason of the exception during exception calculation");
        }
        return y;
    }
}