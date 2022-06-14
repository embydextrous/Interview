package filesystem;

public class Main {
    public static void main(String[] args) throws FileNotFoundException, UnsupportedFileOperationException {
        FileSystem fs = new FileSystem();
        
        fs.mkdir("/users/addam/workspace");
        fs.ls("/");
        fs.addContentToFile("/users/arjit/abc.txt", "This is Arjit's File");
        fs.addContentToFile("/users/arjit/abc.txt", "This is Arjit's File");
        fs.addContentToFile("/users/arjit/def.txt", "This is Arjit's File");
        fs.addContentToFile("/users/arjit/ghi.txt", "This is Arjit's File");
        fs.addContentToFile("/users/arjit/modi.txt", "Madarchod");
        fs.mkdir("/users/sachi/modi");
        fs.ls("/users");
        System.out.println(fs.readContentFromFile("/users/arjit/modi.txt"));
        fs.addContentToFile("/users/arjit/modi.txt", " bhadwa");
        System.out.println(fs.readContentFromFile("/users/arjit/modi.txt"));
    }
}
