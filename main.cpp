#include <iostream>
#include <process.h>

int main()
{
    system("python converter.py");
    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();
    return 0;
}