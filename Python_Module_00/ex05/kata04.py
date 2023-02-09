#!/usr/bin/env python3.7

t = (0, 4, 132.42222, 10000, 12345.67)
msg = 'module_{:02d}, '.format(t[0])
msg += 'ex_{:02d} : '.format(t[1])
msg += '{:03.2f}, '.format(t[2])
msg += '{:.2e}, '.format(t[3])
msg += '{:.2e}'.format(t[4])
print(msg)
