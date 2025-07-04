# 准备
```
 系统安装OpenGL的动态连接库
 sudo apt update
 sudo apt install -y libgl1-mesa-glx

 下载安装conda
 https://www.anaconda.com/docs/getting-started/miniconda/install
 conda create --name idcard python=3.10 
 conda activate idcard
```

# 安装
```
 git clone https://github.com/njskyun/idcard.git
 cd idcard
 pip install -r requirements.txt

 #cartoon-gan
 cd models
 git clone https://github.com/FilipAndersson245/cartoon-gan.git

 #HivisionIDPhotos
 git clone https://github.com/Zeyi-Lin/HivisionIDPhotos.git hivision_id
 cd hivision_id
 pip install -r requirements.txt
 pip install -r requirements-app.txt
 下载人像抠图模型权重文件
 python scripts/download_model.py --models all
```

# cpu上
```
 pip install paddlepaddle -i https://www.paddlepaddle.org.cn/packages/stable/cpu/  安装 PaddlePaddle（CPU） 
 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  安装 pytorch （CPU） 

【改动】
  models/cartoon-gan/predict.py 
 修改  parser.add_argument("-d", "--device", type=str, default="cuda")  
 为：  parser.add_argument("-d", "--device", type=str, default="cpu") 

 修改  pretrained_dir = "./checkpoints/trained_netG.pth"
 为：
 pretrained_dir = os.path.abspath("models/cartoon-gan/checkpoints/trained_netG.pth")

 前往https://drive.google.com/drive/folders/1d_GsZncTGmMdYht0oUWG9pqvV4UqF_kM下载trained_netG.pth并放到models/cartoon-gan/checkpoints/目录下
```

# 运行任务
```
 uvicorn app.main:app --reload  启动
 uvicorn app.main:app  --host 0.0.0.0 --port 8000 --reload 启动外网可访问

 celery -A tasks.worker.celery_app worker --loglevel=info  启动处理队列任务

 celery -A tasks.celery_app.celery_app inspect registered  检查注册列表
```
