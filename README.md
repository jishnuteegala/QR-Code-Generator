# Excel to QR Code Generator

This Python script allows you to generate QR code images from contact details stored in an Excel file. The generated QR code images are saved to a specified folder.

## Prerequisites

Before running the script, ensure that you have Python and the required libraries installed. You can install the libraries using pip. Open your terminal or command prompt and run the following commands:

```bash
pip install pandas
pip install qrcode
pip install pillow
```

## Usage

1. Place your contact data in an Excel file. The Excel file should have columns with the following headers: "Name," "Email," and "Phone." You can modify the code to match your column names if they are different.

2. Edit the script if necessary:
   - Update the `input_excel_file` variable with the path to your Excel file.
   - Update the `output_folder` variable with the path to the folder where you want to save the QR code images.

3. Run the script:

```bash
python generate_qr_code_images.py
```

4. The script will process the Excel file and generate QR codes for each contact. The QR code images will be saved in the specified output folder.

## Example Excel Data

You can use the following example data in your Excel file for testing:

```
Name         Email                        Phone
John Smith   john.smith@example.com       +44 20 1234 5678
Alice Johnson alice.johnson@example.com   +44 20 2345 6789
Bob Brown    bob.brown@example.com        +44 20 3456 7890
Ella Davis   ella.davis@example.com       +44 20 4567 8901
David Wilson david.wilson@example.com     +44 20 5678 9012
Grace Lee    grace.lee@example.com        +44 20 6789 0123
Sam Turner   sam.turner@example.com       +44 20 7890 1234
Olivia White olivia.white@example.com     +44 20 8901 2345
Henry Hall   henry.hall@example.com       +44 20 9012 3456
```

As mentioned in the "Usage" section, make sure to customize the data in your Excel file according to your needs. Ensure that the headers/fields in your Excel File match with the desired contents of each QR Code that is generated and all instances where the field is used to access rows within the pandas dataframe.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
