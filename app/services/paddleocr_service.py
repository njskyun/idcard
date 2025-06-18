from paddleocr import PaddleOCR

# 初始化 OCR 模型，只加载一次
ocr_model = PaddleOCR(use_angle_cls=True, lang='ch')

def recognize_text(image_path):
    try:
        result = ocr_model.ocr(image_path, cls=True)
        texts = []
        for line in result:
            for word_info in line:
                texts.append(word_info[1][0])  # 提取识别文本
        return {"status": "success", "text": texts}
    except Exception as e:
        return {"status": "error", "error": str(e)}
