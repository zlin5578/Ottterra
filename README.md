# Otterra
# Image to 3D Asset with TRELLIS

Thanks to the incredible work of [JeffreyXiang/TRELLIS-image-large](https://huggingface.co/spaces/JeffreyXiang/TRELLIS-image-large), this project leverages the TRELLIS 3D pipeline to generate high-quality 3D assets from a single image.

## Highlights

- **Single-image 3D asset generation**
- **.glb extraction** with mesh simplification and textures
- **.ply extraction** for Gaussian splatting
- **Public API endpoints** for fast, automated generation and download
- Optional background removal with `rembg`
- Experimental support for **multi-view input**

---
## Methodology

1. **Image Input & Preprocessing**
   - Input image is resized and passed through `rembg` for background removal.
2. **3D Reconstruction (TRELLIS)**
   - Uses DINOv2 feature encoding to build latent representations.
   - Structured Latent Array Tokenization (SLAT) reconstructs mesh geometry.
3. **Model Export**
   - Mesh is exported as `.glb` using OpenLRM pipeline.
4. **Unity Scene Integration**
   - `.glb` is imported via `GLTFast` into a pre-built Unity room environment.
   - Drag-and-drop interaction, camera navigation, and layout testing supported.
5. **WebGL Deployment**
   - Scene deployed using Unity WebGL and hosted via Unity Play.

## Usage

### API Endpoints
You can use the Hugging Face space programmatically via `gradio_client` or any HTTP client.

#### 1. `quick_generate_glb`
- Converts a single image to a downloadable `.glb` file (optimized mesh + texture).
- Ideal for real-time applications, web viewers, or AR/VR.

#### 2. `quick_generate_gs`
- Converts an image into a `.ply` file using Gaussian Splatting.
- Great for high-fidelity experimental visualization.

### Example (Python + Gradio Client)

```python
from gradio_client import Client, handle_file

client = Client("JeffreyXiang/TRELLIS")

result = client.predict(
    image=handle_file("your_image_path_or_url.png"),
    api_name="/quick_generate_glb"
)

print("GLB URL:", result)
An AI-driven 3D furniture visualization system that transforms images into interactive 3D models.

## 🚀 Live Demo

Try out the WebGL scene here:  
👉 [Launch WebGL Scene]([https://your-unity-webgl-host.com](https://play.unity.com/en/games/cccfbcc5-f725-483e-ae1e-fd085d33139d/roomscene))

> ⚠️ Best viewed on desktop with Chrome or Firefox.

---

## 📸 Preview

![Demo Screenshot](webgl/preview.png)


## Results & User Feedback

- Full apartment scene (bedroom, living room, kitchen, dining room)
- Interactive manipulation via WebGL
- Time savings: from 1-2 weeks to ~30 minutes
- Est. ~99.6% reduction in manual layout time

### Feedback
> “This tool would have saved me days when I moved last summer!” — User A  
> “The automatic 3D model looks super realistic and loads instantly in the Unity scene.” — User B
