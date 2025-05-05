import qrcode
import cv2
from pyzbar.pyzbar import decode
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)  # For automatic color reset in terminal


def generate_qr(data: str, filename: str = "qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    save_path = Path.cwd() / filename
    img.save(save_path)

    print(f"{Fore.GREEN}[✅] QR Code successfully saved at: {save_path}")


def decode_qr(image_path: str):
    try:
        img = cv2.imread(image_path)
        decoded_objects = decode(img)

        if not decoded_objects:
            print(f"{Fore.RED}[❌] No QR code found in the image.")
            return

        print(f"{Fore.YELLOW}📦 Decoded Results:")
        for obj in decoded_objects:
            print(f"   {Fore.CYAN}-> {obj.data.decode('utf-8')}")
    except Exception as e:
        print(f"{Fore.RED}[⚠️] Error reading image: {e}")


def main():
    print(f"""{Fore.MAGENTA}
    ======================================
        🔳 QR Code Generator & Decoder
    ======================================
    """)

    choice = input(f"{Fore.BLUE}Do you want to [G]enerate or [D]ecode a QR code? ").strip().lower()

    if choice == 'g':
        text = input(f"{Fore.YELLOW}📥 Enter text or URL to generate QR code: ")
        filename = input(f"{Fore.YELLOW}💾 Enter filename to save (default: qrcode.png): ").strip()
        generate_qr(text, filename or "qrcode.png")

    elif choice == 'd':
        image_path = input(f"{Fore.YELLOW}🖼️ Enter path to QR code image: ").strip()
        decode_qr(image_path)

    else:
        print(f"{Fore.RED}[⚠️] Invalid choice. Please select 'g' or 'd'.")

if __name__ == "__main__":
    main()
