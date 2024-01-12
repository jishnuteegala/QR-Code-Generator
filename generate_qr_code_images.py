import pandas as pd
import qrcode
from PIL import Image

# Function to generate QR code from contact details


def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(output_file)

# Function to process Excel file and generate QR codes


def generate_qr_codes_from_excel(input_excel_file, output_folder):
    try:
        df = pd.read_excel(input_excel_file)
        for index, row in df.iterrows():
            contact_data = f"Phone: +{row['Phone']}"
            output_file = f"{output_folder}/+{row['Phone']}.png"
            generate_qr_code(contact_data, output_file)
            print(f"QR code for +{row['Phone']
                                  } generated and saved as {output_file}")
    except Exception as e:
        print(f"Error processing the Excel file: {str(e)}")


if __name__ == "__main__":
    # Change this to your input Excel file
    input_excel_file = r"C:\Users\YourUsername\Documents\contact_data.xlsx"
    # Change this to your desired output folder
    output_folder = r"C:\Users\YourUsername\Documents\QR_Codes"

    generate_qr_codes_from_excel(input_excel_file, output_folder)
