import sys
sys.path.append('../')
from pycore.tikzeng import *
color = r"""
\def\Color1{rgb:yellow,5;red,2.5;white,5}
\def\Color2{rgb:yellow,5;red,5;white,5}"""
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_input('image_clef.png'),
    to_empty(name="image", offset="(-8, 0, 0)", to="(0, 0, 0)"),

    # Vision Transformer block
    to_ConvConvRelu(name='ccr_b1', s_filer=500, n_filer=(64, 64), offset="(-5,0,0)", to="(0,0,0)", width=(12, 12),
                    height=30, depth=30, caption="Vision Transformer", color=1),
    to_connection("image", "ccr_b1"),
    # Quantum Boson Sampler
    to_ConvConvRelu(name='ccr_b2', s_filer=32, n_filer=(1024, 1024), offset="(3,0,0)", to="(ccr_b1-east)",
                    width=(20, 0), height=12, depth=12, caption="Quantum Layer (Boson Sampler)", color=0),
    to_connection("ccr_b1", "ccr_b2"),

    to_ConvConvRelu(name='ccr_b3', s_filer=500, n_filer=(64, 64), offset="(2,0,0)", to="(ccr_b2-east)", width=(3, 0),
                    height=12, depth=12, caption="Linear Layer", color=2),

    to_connection("ccr_b2", "ccr_b3"),


    to_output(name="output", offset="(2, 0, 0)", to="(ccr_b3-east)", caption="Prediction"),
    to_end(),
]

# Generate .tex file
namefile = str(sys.argv[0]).split('.')[0]
to_generate(arch, namefile + '.tex')
