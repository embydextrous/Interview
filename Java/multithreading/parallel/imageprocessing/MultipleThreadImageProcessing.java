package multithreading.parallel.imageprocessing;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import javax.imageio.ImageIO;

public class MultipleThreadImageProcessing {
    public static final String SOURCE_FILE = "/Users/sachi/workspace/Interview/Java/multithreading/parallel/imageprocessing/vvv.jpg";
    public static final String DEST_FILE = "/Users/sachi/workspace/Interview/Java/multithreading/parallel/imageprocessing/vvv_multi.jpg";

    public static void main(String[] args) throws IOException, InterruptedException {
        BufferedImage originalImage = ImageIO.read(new File(SOURCE_FILE));
        BufferedImage resultImage = new BufferedImage(originalImage.getWidth(), originalImage.getHeight(),
                BufferedImage.TYPE_INT_RGB);
        int numCPU = Runtime.getRuntime().availableProcessors();
        ExecutorService executor = Executors.newFixedThreadPool(numCPU);
        int widthPerBlock = originalImage.getWidth() / numCPU;
        long start = System.currentTimeMillis();
        for (int i = 0; i < numCPU; i++) {
            final int c = i;
            executor.submit(new Runnable() {
                @Override
                public void run() {
                    ColorUtil.recolorImage(originalImage, resultImage, c * widthPerBlock, 0, widthPerBlock,
                            originalImage.getHeight());
                }
            });
        }
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);
        long end = System.currentTimeMillis();
        System.out.println("Image processing took " + (end - start) + "ms.");
        File outputFile = new File(DEST_FILE);
        ImageIO.write(resultImage, "jpg", outputFile);
    }
}
