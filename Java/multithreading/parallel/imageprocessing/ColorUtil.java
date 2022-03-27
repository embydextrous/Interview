package multithreading.parallel.imageprocessing;

import java.awt.image.BufferedImage;

public class ColorUtil {

    public static void recolorImage(BufferedImage originalImage, BufferedImage resultImage,
                                     int left, int top, int width, int height) {
        for(int x = left; x < left + width && x < originalImage.getWidth(); x++) {
            for(int y = top; y < top + height && y < originalImage.getHeight(); y++) {
                recolorPixel(originalImage, resultImage, x, y);
            }
        }
    }

    public static void recolorPixel(BufferedImage originalImage, BufferedImage resultImage, int x, int y) {
        int rgb = originalImage.getRGB(x, y);
        int red = red(rgb);
        int green = green(rgb);
        int blue = blue(rgb);

        int newRed = green;
        int newGreen = blue;
        int newBlue = red;
        
        int newRgb = rgb(newRed, newGreen, newBlue);
        setRgb(resultImage, x, y, newRgb);
    }

    private static void setRgb(BufferedImage image, int x, int y, int rgb) {
        image.getRaster().setDataElements(x, y, image.getColorModel().getDataElements(rgb, null));
    }

    public static int red(int rgb) {
        return (rgb & 0x00FF0000) >> 16;
    }

    public static int green(int rgb) {
        return (rgb & 0x0000FF00) >> 8;
    }

    public static int blue(int rgb) {
        return (rgb & 0x000000FF);
    }

    public static int rgb(int red, int green, int blue) {
        int rgb = 0;
        rgb |= blue;
        rgb |= green << 8;
        rgb |= red << 16;
        rgb |= 0xFF000000;
        return rgb;
    }
}
