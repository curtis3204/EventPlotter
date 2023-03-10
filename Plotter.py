import matplotlib.pyplot as plt
import math
import numpy as np
import cv2
from scipy.interpolate import make_interp_spline






#Read file
with open('Event.txt', 'r') as f:
    data = f.readlines()


def data_preprocess(data):
    new_data = []
    for each in data:
        temp = each.split()
        if len(temp) == 3:
            new_data.append(temp[0] + ' ' + temp[1] + ' ' + temp[2])
        elif float(temp[8]) == 0.0000:
            new_data.append(temp[0] + ' ' + temp[1] + ' ' + temp[2])
        else:
            times = float(temp[8])*1000
            for i in range(int(times)):
                new_data.append(temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[3] + ' ' + temp[4]
                                 + ' ' + temp[5] + ' ' + temp[6] + ' ' + temp[7] + ' ' + temp[8])

    with open('New_Event.txt', 'w') as f:
        for each in new_data:
            f.writelines(each)
            f.write('\n')

    return


data_preprocess(data)

with open('New_Event.txt', 'r') as f:
    new_data = f.readlines()


#Data
def Plot_data(data):
        
        lx, ly, rx, ry = [], [], [], []
        l_timestamps = 0
        r_timestamps = 0
        for each in data:
            temp = each.split()
            if 'Left' in each or 'Right' in each:
                if 'Left' in each:
                    lx.append(l_timestamps)
                    ly.append(float(temp[4]))
                    l_timestamps = l_timestamps + 1
                    # left_modified = True
                elif 'Right' in each:
                    rx.append(r_timestamps)
                    ry.append(float(temp[4]))
                    r_timestamps = r_timestamps + 1
                    # right_modified = True

            else:
                # if prev_data_time == 0:
                #     pass
                # elif left_modified or right_modified:
                #     if left_modified and right_modified:
                #         pass
                #     elif left_modified:
                #         rx.append(prev_data_time)
                #         ry.append(0.0)
                #     elif right_modified:
                #         lx.append(prev_data_time)
                #         ly.append(0.0)
                # else:
                lx.append(l_timestamps)
                l_timestamps = l_timestamps + 1
                ly.append(0.0)
                
                rx.append(r_timestamps)
                ry.append(0.0)
                r_timestamps = r_timestamps + 1
                # prev_data_time = temp[1]
                # left_modified = False
                # right_modified = False

        lx, ly, rx, ry = np.array(lx), np.array(ly), np.array(rx), np.array(ry)

        return lx, ly, rx, ry




#Plot
lx, ly, rx, ry = Plot_data(new_data)

print('\nlx: ', lx)
print('\nly: ', ly)
print('\nrx: ', rx)
print('\nry: ', ry)

fig, ax = plt.subplots(2, 1, figsize=(10, 4))
ax[0].set_title('Left Controller')
ax[0].plot(lx, ly)
ax[1].set_title('Right Controller')
ax[1].plot(rx, ry)
# x_major_locator = plt.MultipleLocator((self.end_frame - self.start_frame) / 6)
# ax[0].xaxis.set_major_locator(x_major_locator)
# ax[1].xaxis.set_major_locator(x_major_locator)
ax[0].set_ylim([0, 1.1])
ax[1].set_ylim([0, 1.1])

plt.savefig('EventPlot.png')