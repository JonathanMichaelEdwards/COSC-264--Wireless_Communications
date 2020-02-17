def http_persistent_delay(html_size, num_images, image_size):
    overhead = 200
    roundTripTime = 100*10**-3
    rate = 10*10**6
    connTCP = 200*10**-3

    htmlResponse = ((overhead+html_size) / rate) + ((overhead) / rate) + roundTripTime
    imageResponse = num_images * (((overhead) / rate) + ((overhead+image_size) / rate) + roundTripTime)

    return connTCP + htmlResponse + imageResponse


print("{:.4f}".format(http_persistent_delay(0.5*10**6, 3, 50*10**6)))