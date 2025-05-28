import io
import uuid
import json
import requests
from PIL import Image


class ComfyUIClient:

    def __init__(self, server_address="127.0.0.1:8188"):
        self.server_address = server_address
        self.client_id = str(uuid.uuid4())

    def queue_prompt(self, workflow):
        """将提示加入队列并返回响应"""

        # 1. 加载工作流
        with open(workflow,encoding="utf-8") as f:
            prompt = json.load(f)

        # 2. 发送请求
        url = f"{self.server_address}/prompt"
        print(url)
        payload = {"prompt": prompt, "client_id": self.client_id}
        response = requests.post(url, json=payload)

        # 3. 处理响应
        if response.status_code == 200:
            return response.json()["prompt_id"]
        else:
            raise Exception(f"API Error: {response.text}")
    
    def get_history(self, prompt_id):
        """获取历史记录"""
        url = f"{self.server_address}/history/{prompt_id}"
        response = requests.get(url)
        if len(response.json())>0:
            return response.json()[prompt_id]  # 返回指定prompt_id的历史记录
        else:
            return None
    
    def get_status(self,prompt_id):
    
        history=self.get_history(prompt_id)
        if history is None:
            return None,None
        status=history["status"]
        status_str=status["status_str"]
        completed=status["completed"]
        return status_str,completed

    def get_image(self, filename, subfolder, folder_type,output_name="output.png"):
        """从指定路径获取图像数据"""
        url = f"{self.server_address}/view"
        params = {
            "filename": filename,
            "subfolder": subfolder,
            "type": folder_type
        }
        response = requests.get(url, params=params).content
        Image.open(io.BytesIO(response)).save(output_name)
        print("Download:%s"%output_name)
        return True
    
    def get_images(self,prompt_id):
        outputs=self.get_history(prompt_id)["outputs"]
        for value in outputs.values():
            images=value.get('images',None)
            if images is not None:
                for image in images:
                    filename=image['filename']
                    subfolder=image['subfolder']
                    folder_type=image['type']
                    self.get_image(filename, subfolder, folder_type,filename)


if __name__=="__main__":

    # 初始化client
    server_address=r"http://127.0.0.1:8188:8118"
    client=ComfyUIClient(server_address)

    # 运行工作流
    workflow=r"workflow_api.json"
    prompt_id=client.queue_prompt(workflow)
    print(prompt_id)

    # get history
    # prompt_id=r"9c6ef839-35a2-4775-b61c-76a027f55a88"
    # rst=client.get_history(prompt_id)
    # print(rst)

    # get status
    # prompt_id=r"4677dc6e-2d9f-4204-9d4c-f466442c4357"
    # print(client.get_status(prompt_id))

    # get image view
    # filename='ComfyUI_00083_.png'
    # subfolder=''
    # folder_type='output'
    # client.get_image(filename, subfolder, folder_type)

    # get images
    # prompt_id=r"04d14b75-4e9e-4af0-a398-7eb8037290d6"
    # client.get_images(prompt_id)





