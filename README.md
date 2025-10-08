# plworld_generator

This is a simple Python project that generates random worlds using Perlin-like noise.
It prints the map directly in the terminal using ASCII characters, and can also save a PNG preview.

Each time you run it, it creates a different world with mountains, grasslands, and oceans — all procedurally generated

## Any OS:
Requirements:
```sh
pip install -r requirements.txt
```

Run:
```sh
python main.py
```

You can edit this line in the code to change the world size:
```python
demo(width=240, height=80, scale=0.02, octaves=6, live=True)
```
