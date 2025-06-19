from paddleocr import PaddleOCR
from app.services.llm_service import chat_with_user
from app.services.llm_service import update_system_prompt
# 初始化 OCR 模型，只加载一次  
_ocr_model = None

def get_ocr_model():
    """单例模式获取OCR模型，确保每个进程只加载一次"""
    global _ocr_model
    if _ocr_model is None:
        # 模型只在第一次调用时加载
        _ocr_model =  PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False
        )
    return _ocr_model

 
def recognize_text(image_path):
    try:
        ocr = get_ocr_model()
        result = ocr.ocr(image_path)
        
        texts = ''
        for line in result:   
            for word_info in line['rec_texts']: 
                texts += word_info  # 提取识别文本

        update_system_prompt('1', '你是一个中英文翻译助手，根据用户提供的数据，分析其主要是英文还是中文，来判断翻译目标，如果大部分都是英文，则翻译成中文，反之亦然；翻译出来的东西要符合目标地的文化特色，更容易理解。')
        reply = chat_with_user('1', texts)
        if reply['status'] == 'SUCCESS' : 
            return {"status": "SUCCESS", "result": reply['result']}
        else :
            return {"status": "ERROR", "error": reply['error']}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}
