import pyqrcode
import argparse
import png

parser = argparse.ArgumentParser()
parser.add_argument('--ssid', type=str, required=True)
parser.add_argument('--password', type=str)
parser.add_argument('--auth', type=str, default='WPA')
parser.add_argument('--hidden', type=bool, default=False)

args = parser.parse_args()

def main(args):
    generate(args.ssid, args.password, args.auth, args.hidden)

def generate(ssid, password, auth, hidden):
    qr_text = f'WIFI:T:{auth};S:{ssid};P:{password};H:{hidden};;'
    print(f'[*] Generated QR Code: {qr_text}')

    qr = pyqrcode.create(qr_text)
    qr_file = f'{ssid}.png'
    qr.png(qr_file, scale=5)
    print(f'[*] Saving QRCode: {qr_file}')

if __name__ == '__main__':
    main(args)
