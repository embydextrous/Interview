package filesystem;

/*
 * Design an in-memory file system to simulate the following functions:

    ls: Given a path in string format. If it is a file path, return a list that only contains this file’s name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

    mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don’t exist either, you should create them as well. This function has void return type.

    addContentToFile: Given a file path and file content in string format. If the file doesn’t exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

    readContentFromFile: Given a file path, return its content in string format.
 */

public class FileSystem {
    private static final String FILE_SEPARATOR = "/";

    private File root;

    public FileSystem() {
        this.root = new File(true, "");
    }

    public String readContentFromFile(String filePath) throws FileNotFoundException, UnsupportedFileOperationException {
        File t = root;
        String[] d = filePath.split(FILE_SEPARATOR);
        for(int i = 1; i < d.length; i++) {
            t = t.children.get(d[i]);
            if (t == null) {
                throw new FileNotFoundException("File not found at: " + filePath);
            }
        }
        return t.read();
    }

    public void mkdir(String filePath) {
        File t = root;
        String[] d = filePath.split(FILE_SEPARATOR);
        for(int i = 1; i < d.length; i++) {
            File f = t.children.get(d[i]);
            if (f == null) {
                f = new File(true, d[i]);
                t.children.put(d[i], f);
            }
            t = f;
        }
    }

    public void addContentToFile(String filePath, String content) throws UnsupportedFileOperationException {
        File t = root;
        String[] d = filePath.split(FILE_SEPARATOR);
        for(int i = 1; i < d.length - 1; i++) {
            File f = t.children.get(d[i]);
            if (f == null) {
                f = new File(true, d[i]);
                t.children.put(d[i], f);
            }
            t = f;
        }
        File f = t.children.get(d[d.length - 1]);
        if (f == null) {
            f = new File(false, d[d.length - 1]);
            t.children.put(f.name, f);
        }
        System.out.println(f.name);
        t = f;
        t.append(content);
    }

    public void ls(String filePath) throws FileNotFoundException {
        File t = root;
        String[] d = filePath.split(FILE_SEPARATOR);
        for(int i = 1; i < d.length; i++) {
            t = t.children.get(d[i]);
            if (t == null) {
                throw new FileNotFoundException("File not found at: " + filePath);
            }
        }
        if (t.isDirectory()) {
            for(String name : t.children.keySet()) {
                System.out.println(name);
            }
        } else {
            System.out.println(t.name);
        }
    }
}
