from PIL import Image

# Open the base image and the logo image
base_image = Image.open('D:/vagent/youtubedemos/8dn3m42bnnrge0cmbm4a791z0r.jpeg')
logo = Image.open('D:/vagent/youtubedemos/logo.png')

# Ensure logo maintains transparency
logo = logo.convert('RGBA')

# Resize the logo (using LANCZOS for better quality)
new_size = (300, 300)  # Adjust size as needed
logo = logo.resize(new_size, Image.Resampling.LANCZOS)

# Position for bottom left
position = (100, base_image.size[1] - logo.size[1] - 300)

# Make logo semi-transparent but preserve alpha channel
# Create a copy of the logo to modify
logo_with_opacity = logo.copy()
data = logo_with_opacity.getdata()
new_data = []
for item in data:
    # Preserve original alpha channel ratio while applying new opacity
    new_opacity = int(item[3] * 0.8)  # 0.5 = 50% opacity, adjust as needed
    new_data.append((item[0], item[1], item[2], new_opacity))
logo_with_opacity.putdata(new_data)

# Create transparent layer and composite
transparent = Image.new('RGBA', base_image.size, (0,0,0,0))
transparent.paste(logo_with_opacity, position, logo_with_opacity)
combined = Image.alpha_composite(base_image.convert('RGBA'), transparent)

# Save the result
combined.save('output_image.png')
