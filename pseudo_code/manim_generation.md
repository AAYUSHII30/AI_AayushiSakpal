Manim generation (plain steps)
1. LLM returns structured slides JSON with titles, bullets, narration, and sources.
2. For each slide, fill a Python template: insert title and bullet text.
3. Save each filled template as slide_i.py
4. Optionally, create a master_scene that imports all slides to render in sequence.
5. Run `manim` to render MP4.
