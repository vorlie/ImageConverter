# Image Format Converter

- Download link: [Image-Format-Converter-Setup-v1.1-win32.exe](https://github.com/vorlie/FileFormatConverter/releases/download/v1.1/Image-Format-Converter-Setup-v1.1-win32.exe)
    - The file above works only on Windows 10+

# Using the Program
## 1. Launch the Program:

### 1. First option
- Double-click the `converter.exe` file to launch the "Image Format Converter" program.
- **Context Menu Integration:** Additionally, a context menu item has been added for seamless conversion. ~~Right-click on a supported image file~~ Right-click anywhere, and you should see `Image Format Converter` in your context menu. If you are using Windows 11, click `Show more options` to access this feature.

### 2. Second option
If you dont want to install the app, you can run the source code directly. 
- Download and install [Python 3.12.3](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe).
    - Make sure to add Python to `PATH`.
- Download this repository as `.zip` file. [Click here](https://github.com/vorlie/ImageFormatConverter/archive/refs/heads/main.zip) or clone it.
    - Extract the `.zip`
- Open `Terminal` or `Powershell` inside the extracted or cloned folder and run `pip install -r requirements.txt`. 
- Then open `run_converter.bat` inside the extracted or cloned folder.

## 2. Select Source File:

- Click the button to select the source image file you wish to convert.
## 3. Choose Conversion Format:

- Once the source file is selected, a dropdown menu will display multiple conversion format options, including:
    - PNG to JPEG
    - JPEG to PNG
    - JPEG to WebP
    - WebP to JPEG
    - PNG to WebP
- Select the desired conversion format from the dropdown menu.
## 4. Initiate Conversion:

- After selecting the conversion format, click the "Convert" button to initiate the conversion process.
## 5. Conversion Result:

- The converted image file will be saved in the same directory as the original file, with the appropriate file format extension based on the chosen conversion format.
