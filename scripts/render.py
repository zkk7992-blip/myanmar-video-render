import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def generate_pro_video(input_vid, text_content, output_name):
    clip = VideoFileClip(input_vid)
    txt_clip = TextClip(
        text_content,
        fontsize=70,
        color='white',
        font='fonts/Pyidaungsu.ttf',
        method='caption',
        size=(clip.w * 0.8, None)
    )
    txt_clip = txt_clip.set_position('center').set_duration(clip.duration)
    final = CompositeVideoClip([clip, txt_clip])
    final.write_videofile(output_name, codec="libx264", audio_codec="aac", fps=24)

if __name__ == "__main__":
    generate_pro_video("input/raw.mp4", "မင်းအဆဲခံရတော့မယ်၊ ဆောက်ခွက်", "final_output.mp4")
