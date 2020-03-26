from rpi_message_client.send_message import send_email


gps = (63.422792333333334, 10.400856666666666, '04:59:31, 12/24/2018', 'https://www.google.com/maps/place/63.422792333333334,10.400856666666666', 14.7, 'M')

subject = 'WARNING: Fire Detected'
body = f"Possible fire detected by Forest Fire Finder detected at {gps[2]}\n\n" \
                   f"Google Maps Location:\n{gps[3]}\n\n" \
                   f"Geographical coordinates of drone:\n" \
                   f"Latitude:\t  {gps[0]}\n" \
                   f"Longitude:\t{gps[1]}\n" \
                   f"Altitude:\t   {gps[4]}{gps[5]}"
send_email(subject, body)
