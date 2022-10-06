import pyqrcode
import argparse
import png

parser = argparse.ArgumentParser()
parser.add_argument('--ssid', type=str, required=True)
parser.add_argument('--password', type=str)
args = parser.parse_args()

def main(args):
    generate(args.ssid, args.password)

def generate(ssid, password):
    qr = pyqrcode.create(f'WIFI:T:WPA;S:{ssid};P:{password};;')
    qr.png(f'{ssid}.png', scale=5)

if __name__ == '__main__':
    main(args)
