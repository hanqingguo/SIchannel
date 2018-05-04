import scipy
import numpy as np

f = scipy.fromfile(open("channel_output_bpsk_div_100_dmod"),dtype = scipy.int8)
np.savetxt("channel_output_bpsk_div_100_dmod",f,fmt='%.8f')
