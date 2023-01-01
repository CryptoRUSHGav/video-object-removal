import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension

this_folder = os.path.dirname(os.path.abspath(__file__)) + '/'

Headers = []
Sources = []
Defines = []
Objects = []

if torch.cuda.is_available() == True:
    print("CUDA is available")
    Headers += ['src/ChannelNorm_cuda.h']
    Sources += ['src/ChannelNorm_cuda.c']
    Defines += [('WITH_CUDA', None)]
    Objects += ['ChannelNorm_kernel.o.a']

# if __name__ == '__main__':
#     print("Calling setup()")
#     setup(name='_ext.channelnorm', ext_modules=[
#         CppExtension(
#             name='_ext.channelnorm',
#             # headers=Headers,
#             sources=Sources,
#             extra_objects=Objects
#         )],
#         cmdclass={'build_ext': BuildExtension})

ffi = torch.utils.cpp_extension.CUDAExtension(
    name='_ext.channelnorm',
    sources=Sources,
    define_macros=Defines,
    extra_objects=[os.path.join(this_folder, Object) for Object in Objects]
)

if __name__ == '__main__':
    # ffi.build()
    print(ffi)