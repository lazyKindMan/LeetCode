package qubhjava.test;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import org.junit.jupiter.api.DynamicTest;
import org.slf4j.Logger;
import qubhjava.BaseSolution;
import qubhjava.Testcase;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import static org.testng.Assert.assertEquals;

public class Common {

    public static Testcase[] loadTestcases(Logger log, String problemId, String problemFolder) throws IOException {
        Testcase[] testcases = null;
        FileInputStream fis = null;
        try {
            File file = new File(problemFolder + "/" + problemFolder + "_" + problemId + "/testcase");
            if (!file.exists()) {
                log.info("Problem folder [{}] not found, try premiums...", problemFolder);
                file = new File("premiums/premiums_" + problemId + "/testcase");
            }
            fis = new FileInputStream(file);
            byte[] bytes = fis.readAllBytes();
            // convert to String and split lines
            String content = new String(bytes, StandardCharsets.UTF_8);
            log.info("Loading Testcases for problem {}", problemId);
            String[] splits = content.split("\n");
            JSONArray inputArray = JSON.parseArray(splits[0]);
            JSONArray outputArray = JSON.parseArray(splits[1]);
            testcases = new Testcase[inputArray.size()];
            for (int i = 0; i < inputArray.size(); i++) {
                String inputString = inputArray.getString(i);
                if (inputString.startsWith("\"") && inputString.endsWith("\"")) {
                    inputString = inputString.substring(1, inputString.length() - 1);
                }
                String[] inputSplits = inputString.split("\n");
                testcases[i] = new Testcase(inputSplits, outputArray.get(i));
                log.info("Added {}", testcases[i]);
            }
        } catch (Exception exception) {
            log.error(exception.getMessage(), exception);
        } finally {
            if (fis != null) {
                fis.close();
            }
        }
        return testcases;
    }

    public static DynamicTest addTest(BaseSolution solution, Testcase testcase, String problemId, int idx) {
        return DynamicTest.dynamicTest(
                    String.format("[Problem%s]Testcase%d: %s", problemId, idx, Arrays.toString(testcase.getInput())),
                    () -> assertTimeoutPreemptively(Duration.ofSeconds(3), () -> {
                        Object actual = solution.solve(testcase.getInput());
                        switch (testcase.getOutput()) {
                            case BigDecimal output -> {
                                BigDecimal actualNumber = (BigDecimal) actual;
                                assertEquals(actualNumber.doubleValue(), output.doubleValue(), 1e-4);
                            }
                            case Double output -> assertEquals((Double) actual, output, 1e-4d);
                            case Float output -> assertEquals((Float) actual, output, 1e-4f);
                            case null, default -> assertEquals(actual, testcase.getOutput());
                        }
                    })
            );
    }
}
