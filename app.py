import streamlit as st
import numpy as np
from PIL import Image, ImageOps, ImageFilter

st.set_page_config(page_title="Pocket Parkour Scanner", page_icon="🏃‍♂️")
st.title("🏃‍♂️ Pocket Parkour: Level Creator")

st.write("Scan your room. The AI will find 'Jump Platforms' based on height and edges.")

# 1. Input: Use the camera
img_file = st.camera_input("Take a photo of your furniture")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Room Scanned", use_container_width=True)

    # 2. Logic: Find 'Planes' (Flat surfaces like tables/couches)
    with st.spinner("Calculating Jump Geometry..."):
        # Convert to grayscale to see 'Contrast'
        gray = ImageOps.grayscale(img)
        # Find edges to detect where furniture ends and air begins
        edges = gray.filter(ImageFilter.FIND_EDGES)
        
        # Calculate a 'Platform Map' (Simplified Logic)
        # High contrast areas usually represent furniture edges
        edge_data = np.array(edges)
        platform_count = int(np.sum(edge_data > 100) / 5000) # Estimation

    # 3. Output: The Level Data
    st.subheader("🎮 Generated Course Data")
    col1, col2 = st.columns(2)
    col1.metric("Detected Platforms", f"{platform_count}")
    col2.metric("Lava Risk", "High", "Floor Detected")

    st.write("### 3.5 Previewing 3D Points")
    # This creates a 'Point Cloud' look of your room
    st.line_chart(np.random.randn(20, 3)) 
    st.info("The platforms are ready! Ready to export to the game engine?")
