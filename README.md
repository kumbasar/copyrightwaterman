# copyrightwatermark
Add a copyright watermark to photos. See [referance](https://medium.com/better-programming/add-copyright-or-watermark-to-photos-using-python-a3773c71d431)

## Setup

Install dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

See help:
```bash
./ApplyCopyrightWatermark.py --help
```

```bash                                                  
usage: ApplyCopyrightWatermark.py [-h] [-w WATERMARK] [-s] [-o OUTPUT] [-i INPUT]

optional arguments:
  -h, --help            show this help message and exit
  -w WATERMARK, --watermark WATERMARK
                        Set copyright text (default: © Volkan Kumbasar)
  -s, --show            Show watermarked image (default: False)
  -o OUTPUT, --output OUTPUT
                        Output directory (default: output)
  -i INPUT, --input INPUT
                        Input directory (default: input)
```

## Example

```bash
./ApplyCopyrightWatermark.py --watermark '© Volkan Kumbasar, 2020' --show --output 'out'
```

Checkout the `./out` folder.

### Before
![Before](input/IMG_4937.png)
### After
![After](output/IMG_4937.png)
