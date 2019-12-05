# coding=utf-8
'''
@Author: TJUZQC
@Date: 2019-11-19 10:51:38
@LastAuthor: TJUZQC
@lastTime: 2019-11-22 19:30:51
@Description: None
@FilePath: \ANN\train.py
'''
import os
import numpy as np
from Model import BPNN
from matplotlib import pyplot as plt
import time

log = open('results.log', 'a+')

a=2
b=2
c=2
d=1
def genrate_actual_label(x):
    noise = np.random.normal(0, 0.05, x.shape)
    return a * np.sin(b * x) + c * np.cos(d * x)


sample_domain = (-2*np.pi, 2 * np.pi)
sample_num = 1000
x = np.linspace(sample_domain[0], sample_domain[1], sample_num)
x = np.transpose([x])
y = genrate_actual_label(x)
train_x = np.array(x[0:-1])
train_y = np.array(y[0:-1])
x = np.linspace(sample_domain[0], sample_domain[1], sample_num)
x = np.transpose([x])
y = genrate_actual_label(x)
test_x = np.array(x[0:-1])
test_y = np.array(y[0:-1])
network_structure = [1, 30, 30, 30, 1]
activation = 'tanh'
model = BPNN(network_structure, activation_hidden=activation,
             activation_out='linear')
# model.load_weights('BPNN.npy')
epochs = 90000
learning_rate = 0.003
losses = model.fit(train_x, train_y, epochs=epochs,
                   learning_rate=learning_rate)
plt.plot(losses)
plt.show()
h5_filename = 'net-{}.h5'.format(time.time())
model.save(os.path.join('h5files',h5_filename))
y_pred = model.predict(test_x)
plt.title('y = {a} * np.sin({b} * x) + {c} * np.cos({d} * x), activation is {act}, learning rate is {lr}, epochs is {epochs}'.format(
    act=activation, lr=learning_rate, epochs=epochs, a=a, b=b, c=c, d=d))
plt.scatter(test_x, test_y, label='GT')
plt.plot(test_x, y_pred, color='red', label='predict')
plt.legend()
fig_filename = 'fig-{}.jpg'.format(time.time())
plt.savefig(os.path.join('figures', fig_filename))
log.write('function is : y = {a} * np.sin({b} * x) + {c} * np.cos({d} * x), sample domain: {domain}, sample num : {sample}, network structure is {net_struct}, activation is {act}, learning rate is {lr}, epochs is {epochs}, npy_filename is {h5_filename}, fig_filename is {fig_filename}\n'.format(
    domain=sample_domain, sample=sample_num, net_struct=network_structure, epochs=epochs, h5_filename=h5_filename, fig_filename=fig_filename, act=activation, lr=learning_rate, a=a,b=b,c=c,d=d))
log.close()
plt.show()
