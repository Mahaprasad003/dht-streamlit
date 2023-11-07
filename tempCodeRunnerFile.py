for i in range(1000):
    line = ser.readline().decode('utf-8')
    values = line.split(',')

    humidity = float(values[0])
    temperature = float(values[1].strip())
    print(f"Humidity is: {humidity}, Temperature is: {temperature}")