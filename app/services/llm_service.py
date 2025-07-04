from openai import OpenAI
from app.config import settings
 
client = OpenAI(api_key=settings.ZhipuAI_API_KEY )

redis_client = settings.get_redis_client()

def get_user_prompt(user_id):
    key = f"prompt:{user_id}"
    prompt = redis_client.get(key)
    if not prompt:
        # 默认 system prompt
        prompt = "你是一个聪明的 AI 助手，请简洁、有逻辑地回答用户问题。"
    return prompt

def set_user_prompt(user_id, prompt):
    redis_client.set(f"prompt:{user_id}", prompt)

# 构建完整对话
def get_message_history(user_id, content):
    key = f"chat:{user_id}"
    messages_json = redis_client.get(key)

    if messages_json:
        messages = json.loads(messages_json)
    else:
        # 初次对话，加入用户专属系统提示
        system_prompt = get_user_prompt(user_id)
        messages = [{"role": "system", "content": system_prompt}]

    messages.append({"role": "user", "content": content})
    return messages


# 保存最新对话历史
def save_message_history(user_id, messages, max_turns=2):
    trimmed = messages[-(max_turns * 2 + 1):]
    redis_client.set(f"chat:{user_id}", json.dumps(trimmed))

# 聊天主逻辑
def chat_with_user(user_id, content, update_system_prompt=None):
    try:
        # 如果用户更新了系统 prompt，就更新到 Redis
        if update_system_prompt:
            set_user_prompt(user_id, update_system_prompt)

        messages = get_message_history(user_id, content)

        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=messages,
            stream=False,
            max_tokens=2000
        )

        reply = response.choices[0].message.content

        # 添加 assistant 回复
        messages.append({"role": "assistant", "content": reply})
        save_message_history(user_id, messages)

        return {"status": "SUCCESS", "result": reply}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}