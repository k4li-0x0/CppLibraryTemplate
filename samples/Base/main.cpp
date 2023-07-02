#include <exception>
#include <iostream>
#include "version.h"

class Application {
public:
    void init() {}

    void run() {
        std::cout << PROJECT_NAME << " v" << PROJECT_VERSION << std::endl;
    }

    void shutdown() {}
};

int main(int argc, const char **argv) { 
    try {
        Application app{};
        app.init();
        app.run();
        app.shutdown();
        return 0;
    } catch (const std::exception & e) {
        std::cerr << e.what() << std::endl;
        return -1;
    }
}