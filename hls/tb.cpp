#include <iostream>
#include "cnn_accel.h"

int main(){
    int in[SIZE][SIZE];
    int out[SIZE][SIZE];

    for(int i=0;i<SIZE;i++)
        for(int j=0;j<SIZE;j++)
            in[i][j]=i+j;

    cnn_accel(in,out);

    std::cout<<"Simulation complete"<<std::endl;
    return 0;
}
