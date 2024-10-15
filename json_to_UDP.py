import socket
import json

def send_json_via_udp(json_data, ip, port):
    message = json.dumps(json_data).encode('utf-8')

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        udp_socket.sendto(message, (ip, port))
        print(f"Message sent to {ip}:{port}")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        udp_socket.close()

json_data = [
    {
        "azimuth": 0,
        "height": 0,
        "missionId": 8,
        "missionStatus": 1,
        "windAzimuth": 0,
        "windSpeed": 0,
        "droneId": 1,
        "lastKnownLocation": [
            31.76501002,
            35.08284456
        ],
        "timeOfLastKnownLocation": "2024-10-13T16:24:49.591Z",
        "droneSpeed": 18,
        "nextPlannedLocation": [
            31.767434715757716,
            35.0954818725586
        ]
    }
]

ip = '127.0.0.1'  # Change this to your server's IP
port = 5005  # Change this to your desired port

send_json_via_udp(json_data, ip, port)