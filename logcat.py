#!/usr/bin/python
import base64
import sys
import time

# Use `tail -f logcat.log` to view log in real time

print("Content-Type: text/html")    # HTML is following

print()                             # blank line, end of headers

inject=""
inject = """navigate("css")"""
data = sys.stdin.buffer.read()
with open("logcat.log/" + str(time.time()) +".html","wb") as log:
    log.write(data)
print(inject)
    

