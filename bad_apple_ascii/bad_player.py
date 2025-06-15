import os
import time
import pygame

def main():
    # === SETTINGS ===
    ascii_folder = "ascii_txt"
    audio_file = "bad_apple.mp3"

    print("What FPS works best with your computer?")
    print("I personally think it's best to choose anywhere from 15 to 40")
    print("Just press Enter to use the default value (30).\n")

    # Get input
    FPS = input("FPS? (default = 30): ").strip()
    if not FPS:
        FPS = 30
    else:
        FPS = int(FPS)

    frame_duration = 1 / FPS

    # === LOAD FRAMES ===
    frame_files = sorted(f for f in os.listdir(ascii_folder) if f.endswith(".txt"))
    frames = []
    for filename in frame_files:
        with open(os.path.join(ascii_folder, filename), "r") as f:
            frames.append(f.read())

    total_frames = len(frames)

    # === INIT AUDIO ===
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # === SYNCED PLAYBACK ===
    start_time = time.time()
    for i in range(total_frames):
        # Stay on time
        target_time = start_time + i * frame_duration
        now = time.time()
        sleep_time = target_time - now
        if sleep_time > 0:
            time.sleep(sleep_time)

        print("\033[H", end="")  # Move cursor to top
        print(frames[i])

    print("✅ Done!")
    print("Thanks for watching!!!")

if __name__ == '__main__':
    main()
