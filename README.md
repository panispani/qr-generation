# Generate a QR code from a URL (lasts forever)

## Usage

```bash
# New env
conda create -n qr python=3.9
# Necessary packages
pip install -r requirements.txt
# Run, remember to use your link in this command
python generate_qr.py "https://arxiv.org/abs/2409.09169"
```

QR codes are by default white with transparent background. You can change the fill and back colors by editing lines 7-8 in the code (global *FILL_COLOR* and *BACK_COLOR*)
```python
FILL_COLOR = "white"  # 'black'
BACK_COLOR = "transparent"  # 'white'
```

## Examples
```bash
python generate_qr.py "https://arxiv.org/abs/2409.09169" --format png
python generate_qr.py "https://arxiv.org/abs/2409.09169" --format svg
```

## Current Limitations
For now, SVG supports only transparent white or black QR codes. You can easily get around this by:

1. Non-Transparency: remove this for-loop
```python
for rect in rects:
    rect.parentNode.removeChild(rect)
```

2. Color: Replace "#FFFFFF" with the color of your choice.