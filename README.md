# 【准备】
 python3 -m venv sys 创建虚拟环境
 source sys/bin/activate  激活虚拟环境

# 【安装】
 pip install -r requirements.txt

# 【cpu上需要安装】 
 pip install paddlepaddle -i https://www.paddlepaddle.org.cn/packages/stable/cpu/  安装 PaddlePaddle（CPU） 
 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  安装 pytorch （CPU） 

【cpu上需要改动】
 image_processing_app/models/cartoon-gan/predict.py 
 修改  parser.add_argument("-d", "--device", type=str, default="cuda")   parser.add_argument("-d", "--device", type=str, default="cpu") 


【运行任务】
 uvicorn app.main:app --reload  #启动
 celery -A tasks.worker.celery_app worker --loglevel=info  #处理队列任务
