import os
import numpy as np 
import matplotlib.pyplot as plt
from skimage.transform import resize
from processing.combination import find_difference

def test_find_difference():
    # Caminho das imagens
    current_dir = os.path.dirname(__file__)
    image1_path = os.path.join(current_dir, 'test_image', 'test_image1.jpg')
    image2_path = os.path.join(current_dir, 'test_image', 'test_image2.jpg')

    # Imprimir os caminhos das imagens para verificação
    print(f"Image 1 path: {image1_path}")
    print(f"Image 2 path: {image2_path}")

    # Carregar as imagens
    image1 = plt.imread(image1_path)
    image2 = plt.imread(image2_path)

    # Verificar a forma das imagens antes de redimensionar
    if image1.shape != image2.shape:
        print("Redimensionando a segunda imagem...")
        image2 = resize(image2, image1.shape, anti_aliasing=True)

    # Comparar as imagens
    difference = find_difference(image1, image2)

    # Asserção para garantir que a diferença não seja None
    assert difference is not None, "Diferença não foi calculada corretamente."

    # Adicione uma verificação simples na diferença
    assert np.mean(difference) >= 0, "A diferença deve ser positiva."
