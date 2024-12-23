import os
from rembg import remove
from PIL import Image
from pathlib import Path
import argparse

def remove_background(input_path: str, output_path: str = None):
    """
    Remove background from all images in the input directory
    Args:
        input_path: Path to input directory containing images
        output_path: Optional path to output directory. If None, original images will be overwritten
    """
    # Convert input path to Path object
    input_dir = Path(input_path)
    
    # If output_path is provided, create output directory if it doesn't exist
    if output_path:
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # Supported image formats
    supported_formats = {'.png', '.jpg', '.jpeg', '.webp'}
    
    # Process each image in the input directory
    for img_path in input_dir.iterdir():
        if img_path.suffix.lower() in supported_formats:
            try:
                # Open image
                input_image = Image.open(img_path)
                
                # Remove background
                output_image = remove(input_image)
                
                # Determine output path
                if output_path:
                    output_file = output_dir / f"{img_path.stem}_nobg.png"
                else:
                    output_file = img_path
                
                # Save image with transparent background
                output_image.save(output_file, format='PNG')
                print(f"Processed: {img_path.name}")
                
            except Exception as e:
                print(f"Error processing {img_path.name}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Remove background from images in a directory")
    parser.add_argument("--input_path", help="Path to input directory containing images")
    parser.add_argument("--output_path", help="Optional path to output directory", default=None)
    
    args = parser.parse_args()
    
    remove_background(args.input_path, args.output_path)

if __name__ == "__main__":
    main()