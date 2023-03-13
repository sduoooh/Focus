from typing import Union
import openai
import os
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# 初始化部分
app = FastAPI()


#跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
#各种体的定义
class chatMessege(BaseModel):
    model : Union[str,None] = "chat"
    msg : str

class userInformation(BaseModel):
    userAPI : str

#登录
@app.post("/login/")
async def login(userInput : userInformation):
    openai.api_key = userInput.userAPI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你的交流必须是使用中文的。你是一个可靠的助手。"},
            {"role": "user", "content": "你好"}
        ]
    )
    return {"msg": completion }

#交互
@app.post("/chat/")
async def chat(chatMSG : chatMessege):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你的交流必须是使用中文的。你是一个可靠的助手。"},
            {"role": "user", "content": chatMSG.msg}
        ]
    )
    return {"model" : "chat", "msg" : "OK,I get the messege ," + completion['choices'][0]['message']['content']}



