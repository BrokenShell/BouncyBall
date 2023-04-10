import os
from shutil import rmtree

from PIL import Image
from moviepy.editor import ImageSequenceClip

from app.bounce import bouncing_ball


ball = Image.open(os.path.join("app", "ball.png"))
background = Image.open(os.path.join("app", "bg.png"))
positions = zip(*bouncing_ball(200, 0.725, 50, 1))

img_dir = os.path.join("app", "images")
if os.path.exists(img_dir):
    rmtree(img_dir)
os.mkdir(img_dir)

vid_dir = os.path.join("app", "videos")
if os.path.exists(vid_dir):
    rmtree(vid_dir)
os.mkdir(vid_dir)

for i, (x, y) in enumerate(positions):
    bg = background.copy()
    pos = (200 + round(x), 300 + (100 - round(y)))
    bg.paste(ball, pos, ball)
    bg.save(os.path.join("app", "images", f"ball-{i:0>3}.png"))

clips = sorted(
    os.path.join("app", "images", img)
    for img in os.listdir(os.path.join("app", "images"))
    if img.endswith(".png")
)
sequence = ImageSequenceClip(clips, fps=24)
sequence.write_videofile(
    os.path.join("app", "videos", "bouncing-ball.mp4"),
    fps=24,
    remove_temp=True,
    codec="mpeg4",
)
