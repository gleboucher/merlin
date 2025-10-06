import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define architecture
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('input_image.jpg', name='image-1', to="(-4, 0, 0)", opacity=0.75),  # Replace with your image name if needed
    to_input('input_image.jpg', name='image-2', to="(-4, 0,-2.5)", opacity=0.73),
    to_empty(name="image-2-empty", offset="(0, 0, 0)", to="(-4,0,-2.5)"),
    # PCA Block
    to_SoftMax(name='pca', s_filer=20, offset="(0.8,0,0)", to="(-4,0,0)", caption="PCA", width=1, height=6, depth=6, opacity=0.4),
    to_connection_image( "image-1", "pca"),
    # Quantum Block
    to_ConvConvRelu(name='quantum',  offset="(0.8,0,0)", to="(pca-east)", caption="Quantum Block", width=(4,4), height=6, depth=6),
    to_connection( "pca", "quantum"),
    # MLP Classifier
    to_FullyConnected(name="fc1", s_filer=20, offset="(0.8,0,-1)", to="(quantum-east)", caption="Linear Layer", width=1, height=6, depth=18),
    to_connection( "quantum", "fc1"),
    to_empty(name="no_quantum", offset="(-0.9, 0, 0.2)", to="(fc1-north)"),
    to_skip( "image-2-empty", "no_quantum"),
    to_connection( "no_quantum", "fc1"),
    # Output
    to_output(name="output", offset="(0.8, 0, 0)", to="(fc1-east)", caption="Prediction"),
    to_connection("fc1", "output"),
    to_empty(name="pad_right", offset="(0.7, 0, 0)", to="(output-east)"),
    to_end()
]

# End of architecture
namefile = str(sys.argv[0]).split('.')[0]
to_generate(arch, namefile + '.tex')
