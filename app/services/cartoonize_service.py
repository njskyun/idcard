import os
import subprocess
from app.config import settings

def cartoonize_with_cartoon_gan(input_path):
    input_path  = os.path.abspath(input_path) 
    out_path    = os.path.abspath(settings.OUTPUT_DIR)

    output_dir = os.path.join(out_path, "cartoon_gan")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(input_path))
 
    repo_dir = os.path.abspath("models/cartoon-gan")  # 模型仓库所在目录

    cmd = [
        "python", os.path.join(repo_dir, "predict.py"),
        "-i", input_path,
        "-o", output_path
    ]
    try:
        subprocess.run(cmd, check=True)
        return {"status": "SUCCESS", "result": output_path}
    except subprocess.CalledProcessError as e:
        return {"status": "ERROR", "error": str(e)}
