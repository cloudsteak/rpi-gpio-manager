# Raspberry GPIO manager
GPIO manager for Raspberry PI


## Useful

- https://pinout.xyz
- https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
- https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/issues/277
- https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html

## Dependencies

- Export: 

```bash
pip3 freeze > requirements.txt
```

## Prepare Raspberry PI 

Tested on:
- Raspberry Pi 5
- Raspberry Pi Zero 2 W


### Python 

1. install Python3

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
```

2. Python tools

```bash
sudo apt install --upgrade python3-setuptools
```

3. Install Virtual Environment

```bash
python3 -m pip install --upgrade pip
pip3 install virtualenv
```

```bash
python -m venv env --system-site-packages
```

4. Activate Virtual Environment

```bash
source env/bin/activate
```

### Install Adafruit tools

```bash
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
```

After the reboot the `raspi-blinka.py` is not necessary anymore.


### Check installation

Edit the `blinkatest.py` and modify the pin number in line 11.

Current configuration uses the D23 pin (pin 16/ GPIO 23)
```python
pin = digitalio.DigitalInOut(board.D23)
```

Activate Virtual Environment

```bash
source env/bin/activate
```

Then execute the following command:

```bash
python3 test/blinkatest.py 
```

You need to see this:

```bash
Hello blinka!
Digital IO ok!
I2C ok!
SPI ok!
done!
```


## Run Code

### Relay test

Location: `src/digitalio/relaytest.py`

1. Configure the pins

Create the following environment variables with the correct values:

```bash
RELAY_CHANNEL_COUNT=2
RELAY_PIN_1=D23
RELAY_PIN_2=D24
```

Or create `.env` file (in repository root directory) where you paste the lines above.

2. Activate venv

```bash
source env/bin/activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```

4. Run the relay tester

Code is located in `src` directory

```bash
python3 src/digitalio/relaytest.py 
```

### Led test

Location: `src/digitalio/ledtest.py`

1. Configure the pins

Create the following environment variables with the correct values:

```bash
LED_PIN=D6
```

Or create `.env` file (in repository root directory) where you paste the lines above.

2. Activate venv

```bash
source env/bin/activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```

4. Run the relay tester

Code is located in `src` directory

```bash
python3 src/digitalio/ledtest.py 
```

### Network stability check

Location: `src/network/stability.py`

1. Configure the pins

Create the following environment variables with the correct values:

```bash
NETWORK_STABILITY_HOST=8.8.8.8
NETWORK_STABILITY_PING_INTERVAL=10
NETWORK_STABILITY_PING_COUNT=0
NETWORK_STABILITY_THRESHOLD=3
```

Or create `.env` file (in repository root directory) where you paste the lines above.

2. Activate venv

```bash
source env/bin/activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```

4. Run network check

Code is located in `src` directory

```bash
python3 src/network/stability.py 
```

Solution writes the result to the log file with the following naming convention: `YYYYmmdd-HHMMSS-network.log`