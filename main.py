# Password protection for zip files

import py7zr

def zip_and_password_protect(input_zip, output_zip, password):
    try:
        # Create a password-protected zip archive
        with py7zr.SevenZipFile(output_zip, 'w', password=password) as archive:
            archive.writeall(input_zip)

        print(f"Successfully created and password protected '{output_zip}'")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_zip = "zipped.zip"  # Change to the name the existing zip file
    output_zip = "new_password_protected.zip"  # Change to the desired output zip file name
    password = "your_password"  # Change to the password you want to set

    zip_and_password_protect(input_zip, output_zip, password)
