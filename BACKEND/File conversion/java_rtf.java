package tn.maaoui.domain;
import com.documents4j.api.DocumentType;
import com.documents4j.api.IConverter;
import com.documents4j.job.LocalConverter;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class NewMain {

/**
 * @param args the command line arguments
 * @throws java.io.FileNotFoundException
 */
public static void main(String[] args) throws FileNotFoundException,IOException, InterruptedException, ExecutionException {
	

    ByteArrayOutputStream bo = new ByteArrayOutputStream();
    InputStream in = new BufferedInputStream(new FileInputStream("resume.rtf"));
 
    IConverter converter = LocalConverter.builder()
            .baseFolder(new File(System.getProperty("user.dir") + File.separator +"test"))
            .workerPool(20, 25, 2, TimeUnit.SECONDS)
            .processTimeout(5, TimeUnit.SECONDS)
            .build();

    Future<Boolean> conversion = converter
            .convert(in).as(DocumentType.RTF)
            .to(bo).as(DocumentType.PDF)
            .prioritizeWith(1000) // optional
            .schedule();
    conversion.get();
    try (OutputStream outputStream = new FileOutputStream("model.pdf")) {
        bo.writeTo(outputStream);
    }
    in.close();
    bo.close();
    System.out.print("you did it congratulations....finally");
}

}