/* 
 * File:   main.cpp
 * Author: gidis
 *
 * Created on December 29, 2012, 12:22 PM
 */

#include <cstdlib>

// kyle fix
#include "mylib.hpp"

using namespace std;

int main(int argc, char** argv) {
    // kyle fix
    MyLib* mylib=new MyLib();
    mylib->PrintMessage("hello kyle");
    return 0;
}

