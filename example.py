from PIL import Image
from pathlib import Path

inputPath = Path("D:/PImage/images")
inputFiles = inputPath.glob("**/*.tiff")
outputPath = Path("D:/PImage/opt/icons")


def load_images():
    for f in inputFiles:
        outputFile = outputPath / Path(f.stem + ".jpeg")
        print(f)
        print(outputFile)
        Image.open(f).convert('RGB').save(outputFile)

if __name__ == "__main__":
    load_images()
