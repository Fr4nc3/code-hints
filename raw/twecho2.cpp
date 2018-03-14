// twecho2.cpp
// cpp twecho

#include <iostream>
#include "duper_upper.h"

using namespace std;

int main(int argc, char **argv)
{
    if (argc <= 1)
        return 1;

    DuperUpper du(argc, argv);

    while (!du.end_of_list()) {
        cout << du.arg_normal() << " " << du.arg_upper() << endl;
        du.go_next();
    }

    while (!du.top_of_list()) {
        du.go_prev();
        cout << du.arg_upper() << " " << du.arg_normal() << endl;
    }

    return 0;
}
