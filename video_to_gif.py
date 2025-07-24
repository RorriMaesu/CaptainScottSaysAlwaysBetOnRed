import imageio
import sys

"""
Usage:
    python video_to_gif.py input_video.mp4 output.gif [fps]

- input_video.mp4: Path to the input video file
- output.gif: Path to save the output GIF
- fps (optional): Frames per second for the GIF (default: 10)
"""

def video_to_gif(input_path, output_path, fps=10):
    reader = imageio.get_reader(input_path)
    frames = []
    for frame in reader:
        frames.append(frame)
    imageio.mimsave(output_path, frames, fps=fps)
    print(f"GIF saved to {output_path}")

def batch_convert_videos_to_gifs(directory, fps=10):
    import os
    video_exts = ['.mp4', '.mov', '.avi', '.mkv']
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in video_exts:
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{name}.gif")
            try:
                video_to_gif(input_path, output_path, fps)
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No args: batch convert all videos in current directory
        print("Batch converting all video files in the current directory to GIFs...")
        batch_convert_videos_to_gifs('.', fps=10)
    elif len(sys.argv) < 3:
        print("Usage: python video_to_gif.py input_video.mp4 output.gif [fps]\n       python video_to_gif.py (no args: batch mode)")
        sys.exit(1)
    else:
        input_video = sys.argv[1]
        output_gif = sys.argv[2]
        fps = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        video_to_gif(input_video, output_gif, fps)
