import java.util.Scanner;
import java.io.*;


/**
 * Class Lab1Fodor_KI306 implements an example program for laboratory work #1
 * @author AndryF
 * @version 1.0
 * @since version 1.0
 *
 */
public class Lab1Fodor_KI306 {

    /**
     * The static main method is the entry point to the program
     * @param args command line values
     * @throws FileNotFoundException
     */
    public static void main(String [] args) throws FileNotFoundException {
        char [][] arr;
        int SIZE, iter = 0;
        boolean ok = false;
        Scanner scanner = new Scanner(System.in);
        String symbol;
        File dataFile = new File("MyFile.txt");
        PrintWriter fout = new PrintWriter(dataFile);

        System.out.println("Enter symbol for filling the matrix");
        symbol = scanner.nextLine();
        switch (symbol.length()){
            case 1 -> {
                System.out.println("Now enter the size of matrix");
                SIZE = scanner.nextInt();
                arr = new char[SIZE][];
                for (int i = 0; i < SIZE ; i++) {
                    arr[i] = new char[SIZE-i];
                }

                for (int i = 0; i < SIZE; i++){
                    for (int j = 0; j < SIZE; j++){
                        if (i <= j) {
                            arr[i][j-i] = (char) symbol.codePointAt(0);
                        }
                    }
                }
//                Printing of matrix
                for (int i = 0; i < SIZE; i++){
                    for (int j = 0; j < SIZE; j++){
                        if(i < SIZE/2){
                            if(i <= j){
                                System.out.print(arr[i][j-i] + " ");
                                fout.print(arr[i][j-i] + " ");
                            } else{
                                System.out.print("  ");
                                fout.print("  ");
                            }
                        }else{
                            if(i <= j){
                                if (!ok){
                                    for (int k = 0; k < iter;k++){
                                        System.out.print("  ");
                                        fout.print("  ");
                                    }
                                    ok = true;
                                }
                                System.out.print(arr[i][j-i] + " ");
                                fout.print(arr[i][j-i] + " ");
                            }
                        }

                    }
                    System.out.println();
                    fout.print("\n");
                    if(i >= SIZE/2){
                        iter++;
                        ok = false;
                    }
                }
                fout.flush();
                fout.close();

            }
            case 0 -> {
                System.out.println("You forgot to enter the symbol");
            }
            default -> {
                System.out.println("You entered not a symbol");
            }
        }

    }


}

