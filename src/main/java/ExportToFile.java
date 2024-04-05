import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
//Tyler Patenaude (300338859)
public class ExportToFile {
    public static void run(String s){
        //Code from: https://www.w3schools.com/java/java_files_create.asp
        //Creating the file
        try{
            File myFile = new File("expFile.txt");
            if (myFile.createNewFile()){
                System.out.println("File created: " + myFile.getName() + " at " + myFile.getAbsolutePath());
            }
            else{
                System.out.println("File already exists!");
            }
        }
        catch (IOException e){
            System.out.println("An error occured!");
            e.printStackTrace();
        }
        //Writing to the file with the results from the solved set
        try{
            FileWriter writer = new FileWriter("expFile.txt");
            writer.write(s);
            writer.close();
            System.out.println("Wrote to the file properly!");

            // Running python file
            ProcessBuilder pb = new ProcessBuilder("python3 ./readAndPlay.py");
            pb.start();
        }
        catch (IOException e){
            System.out.println("An error occured!");
            e.printStackTrace();
        }
    }
}
