import cv2
import os

VIDEO_FILE = "bad_apple.mp4"  # Make sure this matches the actual file name

def main():
    # Load video
    cap = cv2.VideoCapture(VIDEO_FILE)

    if not cap.isOpened():
        print(f"❌ Could not open video file: {VIDEO_FILE}")
        exit()

    # Create folder to store frames
    output_folder = "Myframes"
    os.makedirs(output_folder, exist_ok=True)

    frame_num = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        filename = os.path.join(output_folder, f"frame_{frame_num:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Saved {filename}")
        frame_num += 1

    cap.release()
    print(f"🎉 Done! Extracted {frame_num} frames.")

if __name__ == '__main__':
    main()
