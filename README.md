# WebP to PNG Converter

## Editing the Registry File

To add the "WebP to PNG converter" program to the context menu in Windows, follow these steps:

1. Open Notepad or any text editor.
2. Copy the following content:

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\WebP to PNG converter]
@="Convert WebP to PNG"
"Icon"=""PATH TO THE CONVERTER ICO\icon.ico""

[HKEY_CLASSES_ROOT\Directory\Background\shell\WebP to PNG converter\command]
@=""PATH TO THE CONVERTER EXE\converter.exe""
```

3. Replace `"PATH TO THE CONVERTER ICO"` with the path to the folder containing the `icon.ico` file.
4. Replace `"PATH TO THE CONVERTER EXE"` with the path to the folder containing the `converter.py` file.
5. Save the file with a `.reg` extension (e.g., `webp_to_png.reg`).
6. Double-click the `.reg` file to add the context menu entry to the Windows Registry.

## Using the Program

1. Double-click the `converter.exe` file to launch the "WebP to PNG converter" program.
  - If you did set up the context menu correctly, the program should appear in the context menu. Which should be much faster than opening the `converter.exe` file directly. Because you don't need to locate the file on your computer, it's much faster to open it using the context menu :3
2. Click the button "Select WebP file" to select the WebP files you want to convert.
3. The converted PNG file will be saved in the same directory as the original WebP file.

Enjoy converting your WebP images to PNG with ease using the context menu integration!
