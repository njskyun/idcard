from paddleocr import PaddleOCR

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

        print(texts)
        return {"status": "success", "text": texts}
    except Exception as e:
        return {"status": "error", "error": str(e)}
