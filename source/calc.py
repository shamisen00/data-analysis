# %%
import cython
import numpy as np
import cupy as cp
from skimage import data,transform,color

%load_ext Cython
# %%
def sample_func():
    a = 0
    for i in range(100000000):
        a += 1
    return a
# %%
%timeit sample_func()
# %%
%%cython

def sample_func_cython():
    cdef int a = 0
    for i in range(100000000):
        a += 1
    return a
# %%
%timeit sample_func_cython()
# %%
%%cython -a
cdef cy_fib2(int n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a
# %%
%%timeit
import cupy as cp

A = cp.arange(10000).reshape(100, 100).astype('f')
B = cp.arange(10000).reshape(100, 100).astype('f')

D = cp.dot(A, B)
# %%
%%timeit
import numpy as np

A = np.arange(10000).reshape(100, 100).astype('f')
B = np.arange(10000).reshape(100, 100).astype('f')

D = np.dot(A, B)
# %%

np_img = data.coffee()#コーヒーカップ画像をロード

np_img  = transform.resize(np_img, (4096,4096))#4096*4096にリサイズ
np_img = color.rgb2gray(np_img)#グレースケール化
np_img = np_img.astype('f')
cp_img = cp.asarray(np_img)#numpy配列 ⇒ cupy配列に変換
# %%
%timeit np_fimg = np.fft.fftshift(np.fft.fft2(np_img))
# %%
%timeit cp_fimg = cp.fft.fft2(cp_img)
# %%
def sample_func_2():
    index_list = []
    for i in range(2000000):
        index_list.append(i)


def sample_func_3():
    index_list = []
    for i in range(6000000):
        index_list.append(i)

def sample_func_4():
    sample_func_2()
    sample_func_3()
# %%
%%prun
sample_func_4()
# %%
import line_profiler


def sample_func():
    index_list = []

    for i in range(1000000):
        index_list.append(i)

    for i in range(3000000):
        index_list.append(i)

    for i in range(10000000):
        index_list.append(i)


profiler = line_profiler.LineProfiler()
profiler.add_function(sample_func)
_ = profiler.runcall(sample_func)
profiler.print_stats()
# %%
