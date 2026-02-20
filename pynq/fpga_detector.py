from pynq import Overlay, allocate
import numpy as np

overlay = Overlay("cnn_design_wrapper.bit")
dma = overlay.axi_dma_0

def fpga_process(frame):

    gray = frame[:,:,0]
    small = gray[0:64,0:64]

    inbuf = allocate((64,64), dtype=np.int32)
    outbuf = allocate((64,64), dtype=np.int32)

    inbuf[:] = small

    dma.sendchannel.transfer(inbuf)
    dma.recvchannel.transfer(outbuf)

    dma.sendchannel.wait()
    dma.recvchannel.wait()

    return outbuf
