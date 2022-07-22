import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class main {



    public static void main(String[] a) throws IOException {
        int[][] board = loadNums();
        printBoard(board);


    }


    private static void printBoard(int[][] board) {

        for(int i = 0; i<9; i++){

            System.out.print("|");
            for(int j = 0; j<9; j++){
                if(board[i][j] != 0){
                    System.out.print(board[i][j]);
                }
                else{
                    System.out.print(" ");
                }

                if((j+1) % 3 == 0){
                    System.out.print("|");
                }
            }
            if((i+1) % 3 == 0) {
                System.out.println("");
            }
            System.out.println("");
        }
    }


    //Loads the board from system input
    public static int[][] loadNums() throws IOException {

        int[][] board = new int[9][9];

        BufferedReader bi = new BufferedReader(
                new InputStreamReader(System.in)
        );

        for(int i = 0; i <9; i++){
            int num[] = new int[9];
            String[] strNums;
            strNums = bi.readLine().split(" ");

            for(int j = 0; j < strNums.length; j++){
                num[j] = Integer.parseInt(strNums[j]);
            }
            board[i] = num;

        }


        System.out.println("Board Loaded");
        return board;

    }


}
