package multithreading.parallel.imageprocessing;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class SingleThreadImageProcessing {
    public static final String SOURCE_FILE = "/Users/sachi/workspace/Interview/Java/multithreading/parallel/imageprocessing/aaa.jpg";
    public static final String DEST_FILE = "/Users/sachi/workspace/Interview/Java/multithreading/parallel/imageprocessing/aaa_single.jpg";

    public static void main(String[] args) throws IOException {
        BufferedImage originalImage = ImageIO.read(new File(SOURCE_FILE));
        BufferedImage resultImage = new BufferedImage(originalImage.getWidth(), originalImage.getHeight(), BufferedImage.TYPE_INT_RGB);
        long start = System.currentTimeMillis();
        ColorUtil.recolorImage(originalImage, resultImage, 0, 0, originalImage.getWidth(), originalImage.getHeight());
        long end = System.currentTimeMillis();
        System.out.println("Image processing took " + (end - start) + "ms.");
        File outputFile = new File(DEST_FILE);
        ImageIO.write(resultImage, "jpg", outputFile);
    }
}
