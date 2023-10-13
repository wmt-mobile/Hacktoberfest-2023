# Parallel Testing With TestNG and Selenium Webdriver
## Introduction:
Parallel testing has become an indispensable strategy in the modern software testing domain. With ever-growing test suites and shorter development cycles, there's a pressing need to obtain feedback as swiftly as possible. Parallel testing addresses this need by running multiple test cases simultaneously, ensuring faster feedback and efficient resource utilization. Among the tools available, TestNG and Selenium WebDriver stand out as powerful allies to implement this strategy.
## Step-by-Step Guide to Parallel Testing using Selenium WebDriver and TestNG:

###1. Setup the environment:

- Ensure you have the Java Development Kit (JDK) installed.
- Install the IDE( Ecllipse, NetBeans, Jenkins).
- Create a new project Java project with maven.
- Add the following dependecies to your POM file.
- Add the following build plugin to the POM file.
   a.  Selenium
   b. TestNG
   c. Webdriver manager
- Add the following build plugin to the POM file.
```xml
<build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M5</version>
                <configuration>
                    <suiteXmlFiles>
                        <suiteXmlFile>testng.XML</suiteXmlFile>
                    </suiteXmlFiles>
                </configuration>
            </plugin>
		</plugins>
</build>
```
###2. Configuring WebDriver for Parallel Execution:
Parallel execution demands each test to have its unique WebDriver instance. Achieve this using ThreadLocal:
```java
public class DriverFactory {
    private static ThreadLocal<WebDriver> driver = new ThreadLocal<WebDriver>();

    public static WebDriver getDriver() {
        return driver.get();
    }

    public static void setWebDriver(WebDriver driverParm) {
        driver.set(driverParm);
    }
}
```
###3. Writing Test Cases:

Craft your test cases keeping parallel execution in mind.
```java
public class TestClassOne { 
    @BeforeMethod
    public void setup() {
        WebDriver driver = new ChromeDriver();
        DriverFactory.setWebDriver(driver);
    }

    @Test
    public void testMethodOne() {
        WebDriver driver = DriverFactory.getDriver();
        driver.get("https://www.example1.com");
        // Your test steps here
    }

    @AfterMethod
    public void tearDown() {
        WebDriver driver = DriverFactory.getDriver();
        if (driver != null) {
            driver.quit();
        }
    }
}
```
###4. TestNG XML Configuration:
```xml
<suite name="com.mycompany_demoParallelTests_jar_1.0-SNAPSHOT">

    <test name="ParallelClass suite" parallel="classes" thread-count="2">
        
        <classes>
            <class name="TestPackages.TestClassOne"/>
        </classes>
    </test>

</suite>
```
Here, parallel="classes" dictates that each class will execute on a separate thread, with thread-count="2" permitting two parallel threads.
###5. Execute Your Tests:
Run your TestNG suite. You should observe simultaneous execution of your test classes.

