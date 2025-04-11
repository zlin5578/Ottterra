# dbapp/remote_inference.py

from gradio_client import Client, handle_file
from pathlib import Path
import tempfile
from PIL import Image

def remote_trellis_infer(image_pil: Image.Image) -> str:
    """
    调用 HF 空间上的 TRELLIS 模型进行推理，返回视频资源 URL
    """
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        image_pil = image_pil.convert("RGB").resize((512, 512))
        image_pil.save(tmp.name)
        image_path = Path(tmp.name)

    # 初始化 HF Space 客户端（启用 Token）
    client = Client("JeffreyXiang/TRELLIS")

    print("🌀 Step: Calling /image_to_3d to generate video preview...")
    result = client.predict(
        image=handle_file(str(image_path)),
        multiimages=[],
        seed=0,
        ss_guidance_strength=7.5,
        ss_sampling_steps=12,
        slat_guidance_strength=3,
        slat_sampling_steps=12,
        multiimage_algo="stochastic",
        api_name="/image_to_3d"
    )

    print("✅ Success: Video preview URL:", result["video"])
    return result["video"]
