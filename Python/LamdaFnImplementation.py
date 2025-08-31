raw_readings = [19.4, 21.1, 21.7, 18.9, 100.3, 20.5]

calibration_offset = 0.8

outlier_threshold = 30.0

calibrated_readings = [reading + calibration_offset for reading in raw_readings]
filtered_readings = [reading for reading in calibrated_readings if reading <= outlier_threshold]

if filtered_readings:
    average_reading = sum(filtered_readings) / len(filtered_readings)
else:
    average_reading = 0  

print("Calibrated readings:", calibrated_readings)
print("Filtered readings (no outliers):", filtered_readings)
print("Average of filtered readings:", round(average_reading, 2))
