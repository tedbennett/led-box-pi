from websocket import WebSocketApp
import json
import _thread as thread
import sys
import time
from board import Board


class WebSocketClient():
    def __init__(self, host, board):
        self.board = board
        self.socket = WebSocketApp(host,
                                   on_open=lambda ws: self._on_open(ws),
                                   on_close=lambda ws: self._on_close(ws),
                                   on_message=lambda ws, msg: self._on_message(
                                       ws, msg),
                                   on_error=lambda ws, msg: self._on_error(
                                       ws, msg)
                                   )

    def start(self):
        thread.start_new_thread(self.socket.run_forever, ())

    def _on_message(self, ws, message):
        dict = json.loads(message)
        print(dict)
        pattern = dict["pattern"]
        if pattern is not None and len(pattern) == 64:
            print("Pattern accepted")
            # Do something with the pattern
            self.board.set_pattern(pattern)
            # Let server know we received it ok

            def pattern_accepted(*args):
                message = {
                    "type": "pattern accepted",
                    "name": box_name
                }
                self.socket.send(json.dumps(message))
            thread.start_new_thread(pattern_accepted, (self))

    def _on_error(self, ws, error):
        print(error)

    def _on_close(self, ws):
        print("WebSocket closed")

    def _on_open(self, ws):
        print("WebSocket opened")

        def run(*args):
            message = {
                "type": "box connect",
                "name": box_name
            }
            self.socket.send(json.dumps(message))
        thread.start_new_thread(run, ())

        def connect_pattern(*args):
            board.set_pattern(["#008000"] * 64)
            time.sleep(0.1)
            board.set_pattern(["#000000"] * 64)
        thread.start_new_thread(connect_pattern, ())


if __name__ == "__main__":
    box_name = sys.argv[1]
    debug = False if len(sys.argv) <= 2 else sys.argv[2]
    board = Board()

    host = "ws://localhost:5000" if debug else "ws://led-box.herokuapp.com/"
    websocket = WebSocketClient(host, board)
    websocket.start()

    while True:
        board.draw()
