# Icon Generator for My Sahayak PWA
# Run this script to generate app icons from your logo
# Requires: pip install Pillow

from PIL import Image
import os

# Source image - your existing logo
SOURCE_IMAGE = "Screenshot 2025-09-13 232706.png"

# Icon sizes needed for PWA
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

def generate_icons():
    # Create icons directory if it doesn't exist
    os.makedirs("icons", exist_ok=True)
    
    try:
        # Open the source image
        img = Image.open(SOURCE_IMAGE)
        
        # Convert to RGBA if necessary
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        for size in ICON_SIZES:
            # Resize image maintaining aspect ratio
            resized = img.copy()
            resized.thumbnail((size, size), Image.Resampling.LANCZOS)
            
            # Create a new image with exact size and paste the resized image centered
            new_img = Image.new('RGBA', (size, size), (128, 0, 0, 255))  # Maroon background
            
            # Calculate position to center the image
            x = (size - resized.width) // 2
            y = (size - resized.height) // 2
            
            # Paste the resized image
            new_img.paste(resized, (x, y), resized if resized.mode == 'RGBA' else None)
            
            # Save the icon
            output_path = f"icons/icon-{size}x{size}.png"
            new_img.save(output_path, 'PNG')
            print(f"Created: {output_path}")
        
        print("\n✅ All icons generated successfully!")
        print("\nNext steps:")
        print("1. Deploy your website to a hosting service (Netlify, Vercel, etc.)")
        print("2. Go to https://pwabuilder.com")
        print("3. Enter your deployed website URL")
        print("4. Download the Windows package (.msix)")
        print("5. Submit to Microsoft Store via Partner Center")
        
    except FileNotFoundError:
        print(f"Error: Could not find {SOURCE_IMAGE}")
        print("Please make sure the logo file exists in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_icons()
