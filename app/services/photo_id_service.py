import os
import subprocess
from app.config import settings

HV_PATH = os.path.abspath("models/hivision_id")
INF_SCRIPT = os.path.join(HV_PATH, "inference.py")


def generate_id_photo_hivision(input_path): 
    input_path  = os.path.abspath(input_path) 
    out_path    = os.path.abspath(settings.OUTPUT_DIR + "/idcard") 
 

    os.makedirs(out_path, exist_ok=True)
    basename = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(out_path, f"{basename}_idphoto.png")
 
    cmd = [
        "python", INF_SCRIPT,
        "-t", "idphoto",  # 指定证件照类型，自动蓝底
        "-i", input_path,
        "-o", output_path,
        "--height", "413", "--width", "295", 
    ]
    try:
        subprocess.run(cmd, check=True, cwd=HV_PATH)
        return {"status": "SUCCESS", "result": settings.OUTPUT_DIR + f"/idcard/{basename}_idphoto.png"}
    except subprocess.CalledProcessError as e:
        return {"status": "ERROR", "error": str(e)}
