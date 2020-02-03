#!/usr/bin/env python
import asyncio
import websockets

PROMPT="JS> "
HOST="0.0.0.0"
PORT=31337
async def shell(websocket, path):
    print("Client connected " + websocket.remote_address[0], flush=True)
    while True:
        # Currently, in case of multiple connections, just hit empty command
        # and it would break of out this loop and prompt for next connection
        cmd = input(PROMPT)
        if (cmd == ''):
            print("Disconnected")
            print("Waiting for client...", flush=True)
            break
        await websocket.send(cmd)

print("Starting on "+HOST+":"+repr(PORT))
start_server = websockets.serve(shell, HOST, PORT)
print("Waiting for client...", flush=True)
try:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Bye")
    quit()
