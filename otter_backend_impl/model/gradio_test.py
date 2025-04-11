from gradio_client import Client, handle_file

# client = Client("JeffreyXiang/TRELLIS",hf_token="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")
from gradio_client import Client, handle_file

client = Client("tencent/Hunyuan3D-2")
result = client.predict(
		caption=None,
		image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		mv_image_front=None,
		mv_image_back=None,
		mv_image_left=None,
		mv_image_right=None,
		steps=30,
		guidance_scale=5,
		seed=1234,
		octree_resolution=256,
		check_box_rembg=True,
		num_chunks=8000,
		randomize_seed=True,
		api_name="/shape_generation"
)
print(result)
# result = client.predict(
# 		image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
# 		multiimages=[],
# 		seed=0,
# 		ss_guidance_strength=7.5,
# 		ss_sampling_steps=12,
# 		slat_guidance_strength=3,
# 		slat_sampling_steps=12,
# 		multiimage_algo="stochastic",
# 		api_name="/image_to_3d"
# )
# print(result)