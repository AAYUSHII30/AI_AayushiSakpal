# samples/demo_scene.py
from manim import *

class SlideScene(Scene):
    def construct(self):
        # Title
        title = Text("Dynamic Programming", font_size=48)
        self.play(Write(title))
        self.wait(0.5)

        # Bullets
        bullets = [
            "Overlapping subproblems",
            "Optimal substructure",
            "Memoization reduces repeated work"
        ]
        bullet_texts = VGroup(
            *[Text(f"• {b}", font_size=28) for b in bullets]
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(FadeIn(bullet_texts, shift=DOWN))
        self.wait(1)
