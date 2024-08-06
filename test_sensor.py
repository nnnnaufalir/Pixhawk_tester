from dronekit import connect
import time

# Koneksi ke Pixhawk melalui serial port
vehicle = connect('COM9', baud=115200, wait_ready=True)

# Fungsi untuk menampilkan data sensor secara berkala


def get_sensor_data():
    # Dapatkan data GPS
    gps_data = vehicle.location.global_frame
    print(f"GPS: Lat={gps_data.lat}, Lon={gps_data.lon}, Alt={gps_data.alt}")

    # Dapatkan data attitude (roll, pitch, yaw)
    attitude = vehicle.attitude
    print(
        f"Attitude: Roll={attitude.roll}, Pitch={attitude.pitch}, Yaw={attitude.yaw}")

    # Dapatkan data kecepatan (velocity) dalam m/s
    velocity = vehicle.velocity
    print(
        f"Velocity: North={velocity[0]}, East={velocity[1]}, Down={velocity[2]}")

    # Dapatkan data baterai
    battery = vehicle.battery
    print(
        f"Battery: Voltage={battery.voltage}V, Current={battery.current}A, Level={battery.level}%")

    # Dapatkan data eksekusi mode
    mode = vehicle.mode.name
    print(f"Mode: {mode}")


# Loop untuk mengambil data secara berkala
try:
    while True:
        get_sensor_data()
        print("------")
        time.sleep(2)  # Ulangi setiap 2 detik
except KeyboardInterrupt:
    print("Data acquisition stopped by user")

# Menutup koneksi ke Pixhawk
vehicle.close()
