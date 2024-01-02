# rpi-relay-manager
Relay manager for Raspberry PI


## Useful

- https://pinout.xyz
- https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
- https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/issues/277


## Prepare PI 5 

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
sudo apt install python3.11-venv
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

After the reboot the `raspi-blinka.py`` is not necessary anymore.


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

Code is located in `src` directory

```bash
python3 src/relay-test.py 
```