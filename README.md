# 准备
```
 python3 -m venv sys 创建虚拟环境
 source sys/bin/activate  激活虚拟环境
```

# 安装
```
 git clone git@github.com:njskyun/idcard.git
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

# cpu上需要安装 
```
 pip install paddlepaddle -i https://www.paddlepaddle.org.cn/packages/stable/cpu/  安装 PaddlePaddle（CPU） 
 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  安装 pytorch （CPU） 

【改动】
 image_processing_app/models/cartoon-gan/predict.py 
 修改  parser.add_argument("-d", "--device", type=str, default="cuda")  
 为：  parser.add_argument("-d", "--device", type=str, default="cpu") 

 修改  pretrained_dir = "./checkpoints/trained_netG.pth"
 为：
 pretrained_dir = os.path.abspath("models/cartoon-gan/checkpoints/trained_netG.pth") 
```

# 运行任务
```
 uvicorn app.main:app --reload  启动
 celery -A tasks.worker.celery_app worker --loglevel=info  启动处理队列任务

 celery -A tasks.celery_app.celery_app inspect registered  检查注册列表
```
