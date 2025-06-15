import cv2
import os


def main():
    print("What's your preferred width and height?")
    print("Please note that the height should be half the width.")
    print("Just press Enter to use default values (40x20).\n")

    # Get input
    WIDTH = input("Width? (default = 40): ").strip()
    HEIGHT = input("Height? (default = 20): ").strip()

    if not WIDTH:
        WIDTH = 40
    else:
        WIDTH = int(WIDTH)

    if not HEIGHT:
        HEIGHT = 20
    else:
        HEIGHT = int(HEIGHT)

    #To get the right visual effect
    mode = input("are you on dark mode or light mode? ")

    if mode == "dark mode" or "Dark mode" or "DARK MODE":
        ASCII_CHARS = " .:-=+*#%@"  # Dark mode friendly
    else:
        ASCII_CHARS = "@%#*+=-:. "  # Dark mode friendly




    def image_to_ascii(image):
        image = cv2.resize(image, (WIDTH, HEIGHT))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ascii_str = ""
        for row in gray:
            for pixel in row:
                index = min(pixel // 25, len(ASCII_CHARS) - 1)
                ascii_str += ASCII_CHARS[index]
            ascii_str += "\n"
        return ascii_str

    input_folder = "Myframes"
    output_folder = "ascii_txt"
    os.makedirs(output_folder, exist_ok=True)

    files = sorted(f for f in os.listdir(input_folder) if f.endswith(".jpg"))

    for i, filename in enumerate(files):
        path = os.path.join(input_folder, filename)
        frame = cv2.imread(path)
        if frame is None:
            continue
        ascii_frame = image_to_ascii(frame)

        with open(os.path.join(output_folder, f"frame_{i:04d}.txt"), "w") as f:
            f.write(ascii_frame)
        
        print("loading.")
        print(" ")
        print("loading..")
        print(" ")
        print("loading...")
        print(" ")

    print("🎉 All frames converted to ASCII text!")

if __name__ == '__main__':
    main()
