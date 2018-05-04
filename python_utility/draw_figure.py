import matplotlib.pyplot as plt
import numpy as np
import os
import argparse


# filename = "../../Wireless Research/Channel_Test2/channel_input_bpsk_div_100_out"
# filename1 = "../../Wireless Research/Channel_Test2/channel_output_bpsk_div_100_out"



class Draw_figure():
    def __init__(self, test_folder, filename, startline, stopline):

        #print(os.path.dirname(os.path.realpath(__file__)))
        filename = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/' + test_folder + '/' + filename
        with open(filename) as f:
            self.lines = f.readlines()[startline:stopline]

    def draw_figure(self, real, subplot=None):
        self.process_num(real)
        x = np.linspace(start=1, stop=len(self.lines), num=len(self.lines))
        y = self.lines
        if (subplot != None):
            plt.subplot(subplot)
            plt.plot(x, y)

           # for x1, y1 in zip(x, y):
          #      plt.text(x1, y1, str(x1), color="red", fontsize=12)

    def process_num(self, real):
        for idx, val in enumerate(self.lines):
            # print(val[2:13])
            if (real == True):
                self.lines[idx] = val[2:12]
            else:
                self.lines[idx] = val[-14:-3]
                # self.lines[idx] = val[2:12]


if __name__ == '__main__':
    def draw(test_folder, filename, filename_real_part, filename1, filename1_real_part, startline, stopline):
        draw1 = Draw_figure(test_folder, filename, startline, stopline)
        draw1.draw_figure(filename_real_part, 211)


        draw2 = Draw_figure(test_folder, filename1, startline, stopline)
        draw2.draw_figure(filename_real_part, 212)

    parser = argparse.ArgumentParser(description='Draw figures for reult data')
    parser.add_argument('Testfolder', type=str, help='which test folder your data in')
    parser.add_argument('filename', type=str, help='name of which file you want to draw')
    parser.add_argument('--filename_real_part', help='which part want to draw, real or imag', action='store_true')
    parser.add_argument('filename1', type=str, help='second file you want to draw')
    parser.add_argument('--filename1_real_part', help='which part want to draw, real or imag', action='store_true')
    parser.add_argument('--startline', type=int, help='start line of the data', default=1)
    parser.add_argument('--stopline', type=int, help='stop line of the data', default=500)
    parser.add_argument('--draw', dest='draw', action='store_const', const=draw)
    args = parser.parse_args()
    args.draw(args.Testfolder, args.filename, args.filename_real_part, args.filename1, args.filename1_real_part,
              args.startline, args.stopline)
    plt.show()

