from math import sqrt


def bouncing_ball(height, cor, total_time, time_step=0.01):
    g = 9.81
    t = 0
    v = 0
    hmax = height
    h = height
    freefall = True
    t_last = -sqrt(2 * height / g)
    vmax = sqrt(2 * hmax * g)
    y_coords = []
    x_coords = []
    while t < total_time:
        if freefall:
            hnew = h + v * time_step - 0.5 * g * time_step * time_step
            if hnew < 0:
                t = t_last + 2 * sqrt(2 * hmax / g)
                freefall = False
                t_last = t + time_step
                h = 0
            else:
                t = t + time_step
                v = v - g * time_step
                h = hnew
        else:
            t = t + time_step
            vmax = vmax * cor
            v = vmax
            freefall = True
            h = 0
        hmax = 0.5 * vmax * vmax / g
        y_coords.append(h)
        x_coords.append(t)
    return x_coords, y_coords
