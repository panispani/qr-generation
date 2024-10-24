# Generate a QR code from a URL (lasts forever)

```bash
# New env
conda create -n qr python=3.9
# Necessary packages
pip install -r requirements.txt
# Run, remember to use your link in this command
python generate_qr.py "https://arxiv.org/abs/2409.09169"
```

QR codes are by default white with transparent background. You can change them to black by changing the word "white" to "black" (line 23 in the python script).
```python
# From this
img = qr.make_image(fill_color="white", back_color="transparent")
# To this
img = qr.make_image(fill_color="black", back_color="transparent")
```

