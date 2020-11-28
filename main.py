import websocket
import json
try:
    import thread
except ImportError:
    import _thread as thread
import time
import sys
# from luma.core.render import canvas
# from luma.led_matrix.device import ws2812
# import os

box_name = sys.argv[1]
debug = False
if len(sys.argv) > 2:
    debug = sys.argv[2]


def on_message(ws, message):
    dict = json.loads(message)
    print(dict)
    if dict["pattern"] is not None and len(dict["pattern"]) == 64:
        print("Pattern accepted")
        def pattern_accepted(*args):
            message = {
                "type": "pattern accepted",
                "name": box_name
            }
            ws.send(json.dumps(message))

        thread.start_new_thread(pattern_accepted, ())


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        message = {
            "type": "box connect",
            "name": box_name
        }
        ws.send(json.dumps(message))

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    host = "ws://led-box.herokuapp.com/"
    if debug:
        host = "ws://localhost:5000"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

# class Board:
#     def __init__(self):
#         self.device = ws2812(width=8, height=8)
#         self.size = 64
#         self.pattern = ["#000000"] * self.size

#     def set_pattern(self, pattern):
#         if len(pattern) != self.size:
#             return
#         self.pattern = pattern

#     def draw(self):
#         with canvas(self.device) as grid:
#             for index, colour in enumerate(self.pattern):
#                 x = index % 8
#                 y = index // 8
#                 grid.point((x, y), fill=colour)
#             time.sleep(0.05)


# app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# board = Board()


# @socketio.on('message')
# def test_message(message):
#     if message['type'] == 'pattern':
#         pattern = message['data'].split(",")
#         board.set_pattern(pattern)


# @socketio.on('connect')
# def connect():
#     # On connect, flash the pattern green in new thread
#     emit('my response', {'data': 'Connected', 'count': 0})


# @socketio.on('disconnect')
# def disconnect():
#     # On connect, flash the pattern red in new thread
#     print('Client disconnected')


# if __name__ == "__main__":
#     # Fetch the environment variable (so it works on Heroku):
#     socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
#     while True:
#         try:
#             board.draw()
#         except KeyboardInterrupt:
#             pass
