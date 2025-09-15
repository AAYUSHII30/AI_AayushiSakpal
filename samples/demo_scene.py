# samples/demo_scene.py
from manim import *

class SlideScene(Scene):
    def construct(self):
        title = Text("Dynamic Programming", font_size=48)
        bullets = [
            "Overlapping subproblems",
            "Optimal substructure",
            "Memoization reduces repeated work"
        ]
        bullet_texts = VGroup(*[Text(f"• {b}", font_size=28) for b in bullets]).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(title))
        self.wait(0.2)
        self.play(FadeIn(bullet_texts))
        self.wait(1)
