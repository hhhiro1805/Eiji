import discord

TOKEN = "YOUR_TOKEN_HERE"  # Thay bằng token tài khoản người dùng của bạn (KHÔNG chia sẻ)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Đã đăng nhập với {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith("!m2 "):
        content = message.content[4:].strip()
        await message.channel.send(content)
import os
TOKEN = os.getenv("TOKEN")
# Thêm vào main.py hoặc tạo file khác
from fastapi import FastAPI
import threading
import uvicorn

app = FastAPI()

from fastapi.responses import JSONResponse

@app.api_route("/", methods=["GET", "HEAD"])
def read_root():
    return JSONResponse(content={"message": "Selfbot is running"})

def run_web():
    uvicorn.run(app, host="0.0.0.0", port=8080)

# chạy nền webserver
threading.Thread(target=run_web).start()

client.run(TOKEN)
