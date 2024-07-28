# Image Format Converter

## Overview

This project provides two applications for converting and resizing images:

1. **ImageConverter.exe**: A graphical user interface (GUI) application built with PyQt5.
2. **ImageConverterCLI.exe**: A command-line interface (CLI) tool for batch processing images.

Both tools allow users to convert images between different formats and optionally resize them.

## Project Structure

The project directory contains:

- `module/`: Directory containing the image processing logic.
- `cli.py`: Source code for the CLI tool.
- `gui.py`: Source code for the GUI application.
- `requirements.txt`: List of Python dependencies.
- `LICENSE`: License information.
- `README.md`: This file.
- `.gitignore`: Git ignore rules.
- `ImageConverter.spec`: PyInstaller spec file for the GUI application.
- `ImageConverterCLI.spec`: PyInstaller spec file for the CLI tool.

## Downloading the Executables

The compiled executables for Windows are not included in the repository. Instead, you can download them from the GitHub Releases page:

- **[Download ImageConverter.exe (GUI)](https://github.com/vorlie/ImageConverter/releases/download/v1.1/ImageConverterGUI.zip)**
- **[Download ImageConverterCLI.exe (CLI)](https://github.com/vorlie/ImageConverter/releases/download/v1.1/ImageConverterCLI.exe)**

## ImageConverter.exe (GUI)

### Features

- **Select Image File**: Choose an image file from your filesystem.
- **Convert Image Format**: Convert the selected image to one of the supported formats (JPEG, WebP, PNG, GIF, TIFF, BMP).
- **Resize Options**: Optionally resize the image before conversion.
- **Image Preview**: View a preview of the selected image.
- **Convert Button**: Execute the conversion process.

### Running the GUI Application

1. **Download the executable** from the GitHub Releases page.
2. **Run the GUI Application** by double-clicking the `ImageConverter.exe` file.

### Missing Icon

If the icon is missing from the GUI application, download the icon from the GitHub repository and place it under the `./_internal/` directory (that directory **should** be in the same directory as the executable). It should be named `icon.ico`.


## ImageConverterCLI.exe (CLI)

### Features

- **Convert Image Format**: Convert images to various formats from the command line.
- **Resize Options**: Resize images during conversion.

### Running the CLI Tool

1. **Download the executable** from the GitHub Releases page.
2. **Run the CLI Tool** from the command line:

    ```bash
    ./ImageConverterCLI.exe <input_file> <output_format> [--max-width WIDTH] [--max-height HEIGHT]
    ```

    - `<input_file>`: Path to the input image file.
    - `<output_format>`: Desired output format (jpeg, webp, png, gif, tiff, bmp).
    - `--max-width`: Optional maximum width for resizing.
    - `--max-height`: Optional maximum height for resizing.

    **Example**:

    ```bash
    ./ImageConverterCLI.exe myphoto.png jpeg --max-width 800 --max-height 600
    ```

## Development

To contribute to the development or modify the applications:

1. **Clone the Repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd <project-directory>
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Applications**:

    - **GUI Application**:

        ```bash
        python gui.py
        ```

    - **CLI Tool**:

        ```bash
        python cli.py
        ```

5. **Build the Executables**:

    Use PyInstaller to bundle the applications into standalone executables.

    - **For GUI Application**:

        ```bash
        pyinstaller ImageConverter.spec
        ```

    - **For CLI Tool**:

        ```bash
        pyinstaller ImageConverterCLI.spec
        ```

6. **Test the Executables**:

    The built executables will be located in the `dist/` directory. Test them to ensure they work as expected.

## Thanks

A special thanks to the following projects that made this tool possible:

- **[Pillow](https://pillow.readthedocs.io/en/stable/)**: A powerful Python Imaging Library used for opening, manipulating, and saving image files. Version 10.2.0.
- **[PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro)**: A set of Python bindings for Qt libraries used for creating graphical user interfaces. Version 5.15.10.
- **[PyQtDarkTheme](https://pypi.org/project/pyqtdarktheme/)**: A library for applying dark themes to PyQt5 applications. Version 2.1.0.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
