#include "cnn_accel.h"

void cnn_accel(int input[SIZE][SIZE], int output[SIZE][SIZE])
{
#pragma HLS INTERFACE m_axi port=input offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=output offset=slave bundle=gmem
#pragma HLS INTERFACE s_axilite port=return bundle=control

    int kernel[3][3] = {
        {1,0,-1},
        {1,0,-1},
        {1,0,-1}
    };

    for(int i=1;i<SIZE-1;i++){
        for(int j=1;j<SIZE-1;j++){
#pragma HLS PIPELINE
            int sum = 0;

            for(int ki=0;ki<3;ki++){
                for(int kj=0;kj<3;kj++){
                    sum += input[i+ki-1][j+kj-1]*kernel[ki][kj];
                }
            }

            output[i][j]=sum;
        }
    }
}
