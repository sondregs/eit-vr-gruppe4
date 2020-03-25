import serial
import pynmea2
from datetime import datetime


def parse_gps(str):
    for i in range(30):
        str = serialPort.readline().strip().decode('ascii')
        if str.find('GGA') > 0:
            msg = pynmea2.parse(str)
            #print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units))
            lat = msg.latitude
            lon = msg.longitude
            link = "https://www.google.com/maps/place/%s,%s" % (lat,lon)
            #print(f'lat: {lat}, lon: {lon}')
            time = datetime.now().strftime("%H:%M:%S, %m/%d/%Y")
            return lat, lon, time, link, msg.altitude, msg.altitude_units


serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)


def get_gps():
    attempt = 1
    while attempt > 0:
        try:
            attempt=0
            return(parse_gps(str))
        except(UnicodeDecodeError):
            attempt += 1
