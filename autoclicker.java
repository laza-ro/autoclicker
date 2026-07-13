import java.awt.Robot;
import java.awt.event.InputEvent;

public class autoclicker {

    public static void Click(int x, int y) throws Exception {
        try {
            Robot auto = new Robot();
            auto.mouseMove(x, y);
            auto.mousePress(InputEvent.BUTTON1_DOWN_MASK);
            auto.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

}