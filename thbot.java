import java.util.Scanner;
import DiscordClientBuilder

public class thbot {

  public static void main(String[] args) {

    Scanner User_Input = new Scanner(System.in);
    System.out.println("Enter Bot Token:");

    String token = User_Input.nextline();
    System.out.println("Username is: " + token);

    DiscordClientBuilder builder = new DiscordClientBuilder(token);
    DiscordClient client = builder.build();

    client.getEventDispatcher().on(ReadyEvent.class)
        .subscribe(event -> {
          User self = event.getSelf();
          System.out.println(String.format("Logged in as %s#%s", self.getUsername(), self.getDiscriminator()));
        });

    client.login().block();
  }
}
