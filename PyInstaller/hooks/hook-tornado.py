import platform

if platform.system() == "Linux":
    hiddenimports = ["tornado.linux_speedups.websocket_mask"]
else:
    hiddenimports = ["tornado.speedups.websocket_mask"]
