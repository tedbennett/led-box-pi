from websocket import WebSocketApp
import json
import _thread as thread
import sys
from board import Board


class WebSocketClient():
    def __init__(self, host):
        self.socket = WebSocketApp(host,
                                   on_open=lambda ws: self._on_open(ws),
                                   on_close=lambda ws: self._on_close(ws),
                                   on_message=lambda ws, msg: self._on_message(
                                       ws, msg),
                                   on_error=lambda ws, msg: self._on_error(
                                       ws, msg)
                                   )

    def start(self):
        self.socket.run_forever()

    def _on_message(self, ws, message):
        dict = json.loads(message)
        print(dict)
        if dict["pattern"] is not None and len(dict["pattern"]) == 64:
            print("Pattern accepted")
            # Do something with the pattern

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
        print("### closed ###")

    def _on_open(self, ws):
        def run(*args):
            message = {
                "type": "box connect",
                "name": box_name
            }
            self.socket.send(json.dumps(message))
        thread.start_new_thread(run, ())


if __name__ == "__main__":
    box_name = sys.argv[1]
    debug = False if len(sys.argv) <= 2 else sys.argv[2]
    host = "ws://localhost:5000" if debug else "ws://led-box.herokuapp.com/"
    websocket = WebSocketClient(host)

    websocket.start()

    board = Board()
    while True:
        thread.start_new_thread(board.draw, ())
