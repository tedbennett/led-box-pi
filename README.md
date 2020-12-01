# LED Box

This is a script to run on a Raspberry Pi Zero W as part of my LED Box personal project. 

The LED Box is an 8x8 RGB LED matrix which is controlled by a React app at led-box.herokuapp.com. This service supports multiple box connections at once and the ability to select which box to send a pattern to.

## Equipment needed

- Raspberry Pi Zero W (any other Wifi-capable Pi works but is more expensive)
- WS2812 driven 8x8 LED matrix, I used [this one](https://www.amazon.co.uk/dp/B078HYP681/ref=cm_sw_r_oth_api_fabc_9INXFb9RK60Y8?_encoding=UTF8&psc=1)
- 3 wires to connect these devices

The devices are set up by following [this pin guide](https://luma-led-matrix.readthedocs.io/en/latest/install.html#ws2812-neopixels-dma)

## Setup

1. Follow [these steps](https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor) to set up the Pi. I had issues with using the img file to flash, but worked around this by compressing it into a .zip.

2. Set up the luma environment by following [these steps](https://luma-led-matrix.readthedocs.io/en/latest/install.html#installing-from-pypi) (under the heading 'Installing from PyPi'). Don't install `luma.led_matrix` just yet.

3. Once you can connect to the Pi, install git with `sudo apt-get install git`

4. Clone this repo with `git clone https://github.com/tedbennett/led-box-pi.git` and cd into with `cd led-box-pi`

5. Install venv with `sudo apt-get install python3-venv` and csudoreate the Python virtual environment with `python3 -m venv env` and activate it with `source env/bin/activate`

6. Install the required Python libraries. We need to use `sudo` to install the luma libraries and run the script, but `sudo` doesn't use the Python and pip executables from the virtual environment. Use the command `sudo ./env/bin/pip install -r requirements.txt` to install the modules.

7. Run the script with `sudo ./env/bin/python main.py {Name of your LED Box}`

The Box will automatically connect to the server running at led-box.herokuapp.com.