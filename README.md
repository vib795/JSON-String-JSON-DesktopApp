
# JSON String Converter

## Overview
The JSON String Converter is a desktop application built with Python's Tkinter library. It allows users to convert strings to formatted JSON objects and reverse-convert JSON objects into specially escaped JSON strings.

## Requirements
- Python 3.x
- Tkinter (usually comes with Python)
- PyInstaller (for creating an executable)

## Running the Application
To run the application, you need to have Python installed on your system. If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

1. Clone or download the application source code.

2. Navigate to the application directory.

3. Run the application:
    ```bash
    python app.py
    ```

## Features
- Convert a string to a formatted JSON object.
- Reverse-convert a JSON object to a specially escaped JSON string.
- Input and output through a simple GUI.

## Creating an Executable File
To create a standalone executable file for this application, follow these steps:

1. Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2. Navigate to the directory containing your `app.py` file.

3. Run PyInstaller with the following command:
    ```bash
    pyinstaller --onefile --windowed --name json-string-converter app.py
    ```

    - `--onefile` packages the application into a single executable file.
    - `--windowed` is used for GUI applications to prevent the console window from appearing.
    - `--name json-string-json-converter` sets the name of the output executable to `json-string-converter.exe`.

4. After the process completes, find the `json-string-json-converter.exe` file in the `dist` directory.

5. Run the `.exe` file to use the application.

## Notes
- The executable file is platform-specific. If you create the `.exe` on Windows, it will only run on Windows systems.
- The first run of PyInstaller might take longer as it collects all the dependencies. Subsequent runs will be faster.
- Ensure that your antivirus software does not block the executable.
