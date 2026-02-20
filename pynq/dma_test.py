from pynq import Overlay, allocate
import numpy as np

ol = Overlay("cnn_design_wrapper.bit")

dma = ol.axi_dma_0

in_buffer = allocate(shape=(64,64), dtype=np.int32)
out_buffer = allocate(shape=(64,64), dtype=np.int32)

in_buffer[:] = np.random.randint(0,10,(64,64))

dma.sendchannel.transfer(in_buffer)
dma.recvchannel.transfer(out_buffer)

dma.sendchannel.wait()
dma.recvchannel.wait()

print("FPGA Output:", out_buffer[10][10])
