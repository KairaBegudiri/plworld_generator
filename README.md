# plworld_generator

This is a simple Python project that generates random worlds using Perlin-like noise.
It prints the map directly in the terminal using ASCII characters, and can also save a PNG preview.

Each time you run it, it creates a different world with mountains, grasslands, and oceans — all procedurally generated

<img width="2458" height="1331" alt="image" src="https://github.com/user-attachments/assets/41fa2b49-91cd-438f-9896-91c846bdbea6" />


## Any OS:
Requirements:
```python
pip install -r requirements.txt
```

Run:
```python
python main.py
```

You can edit this line in the code to change the world size:
```python
def demo(width=100, height=50, scale=0.04, octaves=6, live=True):
```
