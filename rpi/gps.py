from datetime import datetime

import pynmea2
import serial


def parse_gps():
    for _ in range(30):
        string = serialPort.readline().strip().decode('ascii')
        if string.find('GGA') > 0:
            msg = pynmea2.parse(string)
            #print(f"Timestamp: {msg.timestamp} -- Lat: {msg.lat} {msg.lat_dir} -- Lon: {msg.lon} {msg.lon_dir} -- Altitude: {msg.altitude} {msg.altitude_units}")
            lat = msg.latitude
            lon = msg.longitude
            link = f"https://www.google.com/maps/place/{lat},{lon}"
            #print(f'lat: {lat}, lon: {lon}')
            time = datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
            return lat, lon, time, link, msg.altitude, msg.altitude_units


serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)


def get_gps():
    attempt = 1
    while attempt > 0:
        try:
            attempt = 0
            return parse_gps()
        except UnicodeDecodeError:
            attempt += 1
