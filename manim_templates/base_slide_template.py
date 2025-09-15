# manim_templates/base_slide_template.py
from manim import *

# Template function for generating slides programmatically
def make_slide(title, bullets):
    class GeneratedSlide(Scene):
        def construct(self):
            title_text = Text(title, font_size=48)
            bullet_texts = VGroup(
                *[Text(f"• {b}", font_size=28) for b in bullets]
            ).arrange(DOWN, aligned_edge=LEFT)
            
            self.play(Write(title_text))
            self.wait(0.5)
            self.play(FadeIn(bullet_texts, shift=DOWN))
            self.wait(1)
    return GeneratedSlide
