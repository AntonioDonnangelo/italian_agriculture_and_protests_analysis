from PIL import Image

def create_gif(image_paths, output_gif_path, duration=500):
 images = [Image.open(image_path) for image_path in image_paths]
# Save as GIF
 images[0].save(
 output_gif_path,
 save_all=True,
 append_images=images[1:],
 duration=duration,
 loop=0 # 0 means infinite loop
 )

if __name__ == "__main__":
 # List of image file paths
 image_paths = ["2015.jpg", "2016.jpg", "2017.jpg", "2018.jpg", "2019.jpg", "2020.jpg", "2021.jpg", "2022.jpg", "2023.jpg"] # Add your file paths

# Output GIF path
 output_gif_path = "LUC_GIF_TUSCANY.gif"
# Create GIF
 create_gif(image_paths, output_gif_path)

print(f"GIF created and saved as {output_gif_path}")