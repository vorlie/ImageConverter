#include   <iostream>
#include   <process.h>

const std::string WARNING_MESSAGE = "WARNING: This program may not work if Python or pip is not installed.\n"
                                      "Please download and install Python 3.12.3 from <https://www.python.org/downloads/>.\n"
                                      "Make sure to add the Python installation directory to your PATH environment variable, and disable any path length limit restrictions.\n";
                                      
const std::string NOTE_MESSAGE = "NOTE: If you are sure you have Python installed, check if your PATH environment variable contains these directories:\n";
const std::string COMMON_PYTHON_PATH = "Common Python path is: C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Python\\Python312\\\n";
const std::string COMMON_PYTHON_SCRIPTS_PATH = "Common Python Scripts path is: C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\\n";
const std::string SEPARATOR = "==========";

int main() {
    std::cout << WARNING_MESSAGE ;
    std::cout << "\n" << NOTE_MESSAGE;
    std::cout << "\n" << COMMON_PYTHON_PATH << COMMON_PYTHON_SCRIPTS_PATH << "\n";
    std::cout << SEPARATOR << "\n\n";

    bool pythonInstalled = false;
    try {
        system("python --version");
        pythonInstalled = true;
    } catch (const std::runtime_error& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    if (pythonInstalled) {
        system("pip install -r requirements.txt");
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }

    return 0;
}