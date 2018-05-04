import os
import argparse
import scipy
import numpy as np

##########################################################
# usage:
# python load_binary.py filename test_folder --isByte(if complex, don't add this) -destpath output path --load
##########################################################


dir_path = os.path.dirname(os.path.realpath(__file__))
upper_path = os.path.dirname(dir_path)+'/'
test_folder = 'Channel_Test1/'


# os.path.realpath(__file__) = /home/hanqing/Wireless Research/python_utility/load_binary.py
# dir_path = /home/hanqing/Wireless Research/python_utility
# upper_path = /home/hanqing/Wireless Research


def load(filename, test_folder, isByte, destpath):

    load_file = os.path.join(upper_path,test_folder,filename)
    fullDestPath = upper_path + destpath + '/' + filename +'_out'
    print("Full path of output file is {}".format(fullDestPath))
    print("is this Byte source? {}".format(isByte))
    if(isByte):
        f = scipy.fromfile(open(load_file), dtype = scipy.int8)
        print("Read the file {}".format(load_file))
        np.savetxt(fullDestPath, f, fmt= '%.8f')
        print("Save the result to {}".format(fullDestPath))
    else:
        f = scipy.fromfile(open(load_file), dtype = scipy.complex64)
        print("Read the file {}".format(load_file))
        np.savetxt(fullDestPath, f, fmt = '%.8f')
        print("Save the result to {}".format(fullDestPath))



parser = argparse.ArgumentParser(description='Specify which file to load, complex or float')
parser.add_argument('filename', type=str, help = 'name of which file you want to load')
parser.add_argument('test_folder', type = str, help = 'name of which folder you want to load')
parser.add_argument('--isByte',  help = 'byte file or not', action = 'store_true')

#parser.add_argument('--isByte', type = str, default = 'False')


#"Without --isByte, then load complex file"
#"With --isByte, then load byte file"
parser.add_argument('-destpath',type=str,help = 'output dir-path',default=test_folder)
parser.add_argument('--load',dest = 'load', action='store_const',const = load)
args = parser.parse_args()
args.load(args.filename,args.test_folder, args.isByte,args.destpath)

