#ifndef CNN_ACCEL_H
#define CNN_ACCEL_H

#include <ap_int.h>
#include <hls_stream.h>

#define SIZE 64

void cnn_accel(int input[SIZE][SIZE], int output[SIZE][SIZE]);

#endif
