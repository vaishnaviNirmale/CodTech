import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def introduction():
    speak("Welcome to 'The Enchanted Labyrinth'!")
    time.sleep(1)
    speak("You are an adventurer seeking the legendary treasure hidden deep within the labyrinth.")
    time.sleep(1)
    speak("Your journey begins now...")
    time.sleep(1)

def whispering_hallway():
    speak("\nYou enter a hallway with mysterious whispers.")
    time.sleep(1)
    speak("Some whispers guide you, while others may lead to deadly traps.")
    time.sleep(1)
    speak("Do you follow Whisper A or Whisper B? ")
    choice = input("Do you follow Whisper A or Whisper B? (A/B): ").upper()

    if choice == 'A':
        speak("You follow Whisper A and avoid a hidden pitfall. Well done!")
    elif choice == 'B':
        speak("Unfortunately, Whisper B leads you into a trap. You lose a life.")
        return False
    else:
        speak("Invalid choice. Please enter 'A' or 'B'.")
        return whispering_hallway()

    return True


def illusionary_bridge():
    speak("\nYou reach a seemingly broken bridge over a chasm.")
    time.sleep(1)
    speak("Solve the riddle to reveal the true path.")
    time.sleep(1)
    speak("What has keys but can't open locks? ")
    answer = input("What has keys but can't open locks? ").lower()

    if answer == "keyboard":
        speak("Correct! The illusionary bridge disappears, revealing the safe path.")
    else:
        speak("Incorrect answer. The illusionary bridge collapses, and you lose a life.")
        return False

    return True


def guardians_riddle():
    speak("\nYou encounter a guardian who poses a riddle.")
    time.sleep(1)
    speak("Answer correctly to proceed.")
    time.sleep(1)
    speak("The more you take, the more you leave behind. What am I?")

    answer=input("The more you take, the more you leave behind. What am I?").lower()

    if answer == "footsteps":
        speak("Correct !The guardian is pleased. You may pass.")
    else:
        speak("Incorrect answer .The guardian is angered. You must face a battle!")
        return False

    return True


def mirror_maze():
    speak("\nYou enter a room filled with mirrors, creating a confusing maze.")
    time.sleep(1)
    speak("Some mirrors reflect the true path, while others create illusions.")
    time.sleep(1)
    speak("Do you use a lantern to reveal the real reflections?")
    choice = input("Do you use a lantern to reveal the real reflections? (Y/N): ").upper()

    if choice == 'Y':
        speak("Your lantern reveals the real reflections, and you navigate through the maze safely.")
    elif choice == 'N':
        speak("Without the lantern, you choose the wrong path and fall into a pit. You lose a life.")
        return False
    else:
        speak("Invalid choice. Please enter 'Y' or 'N'.")
        return mirror_maze()

    return True


def doppelgangers_dilemma():
    speak("\nYou encounter a magical doppelganger mimicking your every move.")
    time.sleep(1)
    speak("You must figure out how to exploit its weakness.")
    time.sleep(1)
    speak("Do you observe its movements or attack directly?")
    choice = input("Do you observe its movements or attack directly? (O/A): ").upper()

    if choice == 'O':
        speak(
            "You observe its movements and discover its weakness. You outsmart the doppelganger and claim the treasure!")
    elif choice == 'A':
        speak("Attacking directly triggers a countermove. You lose a life in the confrontation.")
        return False
    else:
        speak("Invalid choice. Please enter 'O' or 'A'.")
        return doppelgangers_dilemma()

    return True


def main():
    introduction()

    # Start the adventure
    doppelganger_result = None  # Initialize to None
    if whispering_hallway():
        if illusionary_bridge():
            if guardians_riddle():
                if mirror_maze():
                    doppelganger_result = doppelgangers_dilemma()

    # Display the final outcome
    if doppelganger_result is not None:
        speak("\nCongratulations! You have successfully navigated 'The Enchanted Labyrinth' and claimed the legendary "
              "treasure!")
    else:
        speak("\nGame over. The labyrinth claims another unfortunate explorer.")

if __name__ == "__main__":
    main()
