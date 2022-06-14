package filesystem;

import java.util.HashMap;

public class File {
    private boolean directory;
    HashMap<String, File> children = new HashMap<>();
    String name;
    private String content = "";
    
    public File(boolean directory, String name) {
        this.directory = directory;
        this.name = name;
    }

    public boolean isDirectory() {
        return directory;
    }

    public String read() throws UnsupportedFileOperationException {
        if (isDirectory()) {
            throw new UnsupportedFileOperationException("Cannot read contents from a directory");
        }
        return content;
    }

    public void append(String appendContent) throws UnsupportedFileOperationException {
        if (isDirectory()) {
            throw new UnsupportedFileOperationException("Cannot write content to a directory");
        }
        StringBuilder sb = new StringBuilder(content);
        sb.append(appendContent);
        content = sb.toString();
    }
}
