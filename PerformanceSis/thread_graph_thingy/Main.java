import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.imageio.ImageIO;

public class Main {
    public static final String ARQUIVO_ORIGEM = "./resources/image.png";
    public static final String ARQUIVO_DESTINO = "./resources/image_out.png";

    public static void main(String[] args) throws IOException {
        BufferedImage ImagemOriginal = ImageIO.read(new File(ARQUIVO_ORIGEM));
        BufferedImage ImagemResultado = new BufferedImage(ImagemOriginal.getWidth(), ImagemOriginal.getHeight(),
                BufferedImage.TYPE_INT_RGB);

        // tempo no inicio da execução
        // long startTime = System.currentTimeMillis();
        // recolorirUmaThread(ImagemOriginal, ImagemResultado);

        File outputFile = new File(ARQUIVO_DESTINO);
        int numberOfThreads = 6;
        for (int i = 1; i <= 10; i++) {
            long startTime = System.currentTimeMillis();
            recolorMultithreaded(ImagemOriginal, ImagemResultado, numberOfThreads, i);
            long endTime = System.currentTimeMillis();
            long duration = endTime - startTime;
            ImageIO.write(ImagemResultado, "jpg", outputFile);
            System.out.println("Tempo de execução: " + duration + "ms");
            System.err.println("Threads usadas: " + 6);
            System.out.println("Imagem reudiza em: " + i + "x");
        }

        System.out.println("Processando com uma thread");

        // single-threaded example
        for (int i = 1; i <= 10; i++) {
            long startTime = System.currentTimeMillis();
            recolorMultithreaded(ImagemOriginal, ImagemResultado, 1, i);
            long endTime = System.currentTimeMillis();
            long duration = endTime - startTime;
            ImageIO.write(ImagemResultado, "jpg", outputFile);
            System.out.println("Tempo de execução: " + duration + "ms");
            System.err.println("Threads usadas: " + 1);
            System.out.println("Imagem reudiza em: " + i + "x");
        }
        // int numberOfThreads = 4;
        // recolorMultithreaded(ImagemOriginal, ImagemResultado, numberOfThreads);
        // recolorFracionado(ImagemOriginal, ImagemResultado, numberOfThreads);
        // try (FileWriter writer = new FileWriter("result.txt")) {
        // writer.append("Tempo de execução: " + duration + "ms\n");
        // writer.append("Threads usadas: " + numberOfThreads + "\n");
        // }

    }

    public static void recolorFracionado(BufferedImage ImagemOriginal,
            BufferedImage ImagemResultado, int partes) {
        int width = ImagemOriginal.getWidth();
        int height = ImagemOriginal.getHeight() / partes;
        for (int i = 0; i < partes; i++) {
            final int multiplicadorInicio = i;
            int xInicio = 0;
            int yInicio = height * multiplicadorInicio;
            recolorirImagem(ImagemOriginal, ImagemResultado, xInicio, yInicio,
                    width, height);
        }
    }

    public static void recolorMultithreaded(BufferedImage ImagemOriginal,
            BufferedImage ImagemResultado, int numberOfThreads, int divideBy) {
        // lista de threads usadas pra executar o código
        List<Thread> threads = new ArrayList<>();
        int width = ImagemOriginal.getWidth() / divideBy;
        int height = ImagemOriginal.getHeight() / (numberOfThreads * divideBy);

        for (int i = 0; i < numberOfThreads; i++) {
            final int threadMultiplier = i;
            Thread thread = new Thread(() -> {
                int xOrigin = 0;
                int yOrigin = height * threadMultiplier;
                recolorirImagem(ImagemOriginal, ImagemResultado, xOrigin, yOrigin,
                        width, height);
            });
            threads.add(thread);
        }
        for (Thread thread : threads) {
            thread.start();
        }
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());
            }

        }
    }

    public static void recolorirUmaThread(BufferedImage ImagemOriginal,
            BufferedImage ImagemResultado) {
        recolorirImagem(ImagemOriginal, ImagemResultado, 0, 0,
                ImagemOriginal.getWidth(), ImagemOriginal.getHeight());
    }

    public static void recolorirImagem(BufferedImage ImagemOriginal, BufferedImage ImagemResultado, int leftCorner,
            int topCorner,
            int width, int height) {
        for (int x = leftCorner; x < leftCorner + width && x < ImagemOriginal.getWidth(); x++) {
            for (int y = topCorner; y < topCorner + height && y < ImagemOriginal.getHeight(); y++) {
                recolorirPixel(ImagemOriginal, ImagemResultado, x, y);
            }
        }
    }

    public static void recolorirPixel(BufferedImage ImagemOriginal, BufferedImage ImagemResultado, int x, int y) {
        int rgb = ImagemOriginal.getRGB(x, y);
        int red = getRed(rgb);
        int green = getGreen(rgb);
        int blue = getBlue(rgb);
        int newRed;
        int newGreen;
        int newBlue;
        // aqui vamos popular os novos pixels
        // se o pixel em quest o for um tom de cinza, vamos aumentar o n vel de� �
        // vermelho em 10; o de verde diminuir 80, azul dimiuir 20
        if (ehNivelDeCinza(red, green, blue)) {
            // para n o exceder o valor m ximo (255) pegamos o min� �
            newRed = Math.min(255, red - 22);
            newGreen = Math.max(0, green - 20);
            // para n o passar o 0 pegamos o max�
            newBlue = Math.max(0, blue - 10);
        } else {
            newRed = red;
            newGreen = green;
            newBlue = blue;
        }
        // M todo para setar valor rgb na coordenada do pixel da imagem�
        int newRGB = createRGBFromColors(newRed, newGreen, newBlue);
        setRGB(ImagemResultado, x, y, newRGB);
    }

    public static void setRGB(BufferedImage image, int x, int y, int rgb) {
        image.getRaster().setDataElements(x, y,
                image.getColorModel().getDataElements(rgb, null));
    }
    // metodo para verificar se o pixel tom de cinza (estar na parte branca da� �
    // flor)
    // // Checa se todos os componentes tem uma intensidade similar (< 30 -
    // determinado
    // empiricamente)

    public static boolean ehNivelDeCinza(int red, int green, int blue) {
        return Math.abs(red - green) < 30 && Math.abs(red - blue) < 30 && Math.abs(
                green - blue) < 30;
    }

    public static int createRGBFromColors(int red, int green, int blue) {
        int rgb = 0;
        // opera o de OR deslocando para esquerda em cada cor��
        rgb |= blue;
        rgb |= green << 8;
        rgb |= red << 16;
        rgb |= 0xFF000000;
        return rgb;
    }

    public static int getRed(int rgb) {
        return (rgb & 0x00FF0000) >> 16;
    }

    public static int getGreen(int rgb) {
        return (rgb & 0x0000FF00) >> 8;
    }

    public static int getBlue(int rgb) {
        return rgb & 0x000000FF;
    }
}