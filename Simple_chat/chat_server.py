import asyncio
import websockets
import json
import os
from datetime import datetime, timezone, timedelta 

HISTORY_FILE = 'chat_history.json'
HISTORY_DURATION = timedelta(days=12) 

# Load existing history or initialize
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r') as f:
        message_history = json.load(f)
else:
    message_history = []

connected = set() 

def save_history_sync():
    with open(HISTORY_FILE, 'w') as f:
        json.dump(message_history, f) 

async def cleanup_history():
    global message_history
    cutoff = datetime.now(timezone.utc) - HISTORY_DURATION
    new_history = []
    for msg in message_history:
        # Parse timestamp string into timezone-aware datetime
        msg_time = datetime.fromisoformat(msg['timestamp'])
        # Ensure it's timezone-aware
        if msg_time.tzinfo is None:
            msg_time = msg_time.replace(tzinfo=timezone.utc)
        if msg_time > cutoff:
            new_history.append(msg)
    message_history = new_history
    save_history_sync() 

async def send_history(websocket):
    for msg in message_history:
        await websocket.send(msg['content']) 

async def broadcast_user_count():
    user_count = len(connected)
    message = f"USER_COUNT:{user_count}"
    for conn in connected:
        try:
            await conn.send(message)
        except:
            pass
        
async def chat(websocket):
    print("Client connected")
    connected.add(websocket)
    try:
        # Send chat history
        await send_history(websocket)
        # Notify all clients of new user count
        await broadcast_user_count()
        async for message in websocket:
            print(f"Received message from {websocket.remote_address}: {message}")
            timestamp = datetime.now(timezone.utc).isoformat()
            # Save message with timestamp
            message_obj = {'content': message, 'timestamp': timestamp}
            message_history.append(message_obj)
            save_history_sync()
            await cleanup_history()
            # Broadcast message to others
            for conn in connected:
                if conn != websocket:
                    try:
                        await conn.send(message)
                    except Exception as e:
                        print(f"Error sending message to a client: {e}")
                        # Optionally, remove the broken connection
                        # connected.remove(conn)
    except Exception as e:
        print(f"Error in websocket connection: {e}")
    finally:
        if websocket in connected:
            connected.remove(websocket)
        print("Client disconnected")
        await broadcast_user_count()

async def main():
    print("Chat Server starting...")
    async with websockets.serve(chat, "0.0.0.0", 8765, ping_interval=20):
        print("Server running on ws://0.0.0.0:8765")
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(main())