def http_nonpersistent_delay(html_size, num_images, image_size):
    overhead = 200
    roundTripTime = 100*10**-3
    rate = 10.0*10**6
    connTCP = 200*10**-3

    connSetUp = (num_images+1) * connTCP   # add 1 for the http request and response
    htmlResponse = ((overhead+html_size) / rate) + ((overhead) / rate) + roundTripTime
    imageResponse = num_images * (((overhead) / rate) + ((overhead+image_size) / rate) + roundTripTime)

    return connSetUp + htmlResponse + imageResponse

print("{:.4f}".format(http_nonpersistent_delay(0.5*10**6, 3, 50*10**6)))
