from PIL import Image
from pathlib import Path

inputPath = Path("D:/PImage/images")
inputFiles = inputPath.glob("**/*.tiff")
outputPath = Path("D:/PImage/opt/icons")

def load_images():
    for f in inputFiles:
        outfile = outputPath / Path(f.stem + ".jpeg")
        Image.open(f).convert('RGB').resize((128, 128)).rotate(270).save(outfile)

if __name__ == "__main__":
    load_images()
