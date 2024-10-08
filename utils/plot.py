import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def plot_image(image):
    """
    Plota uma imagem diretamente, assumindo que ela já foi carregada como array NumPy.
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    """
    Plota várias imagens lado a lado, com a última sendo o resultado de uma operação.

    Args:
        *args: Imagens para plotar.
    """
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    names_lst.append('Result')
    
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    """
    Plota os histogramas dos três canais (vermelho, verde, azul) de uma imagem.

    Args:
        image (PIL.Image or np.array): Imagem para plotar os histogramas.
    """
    # Verifica se a imagem é do tipo PIL e a converte para um array NumPy
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    # Certifique-se de que a imagem seja colorida (3 canais)
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("A imagem deve ter 3 canais (RGB).")
    
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f'{color.title()} Histogram')
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    
    fig.tight_layout()
    plt.show()

def plot_combined_result(image1, image2, combined_image):
    """
    Plota duas imagens originais e a imagem combinada lado a lado.

    Args:
        image1 (np.array): Primeira imagem.
        image2 (np.array): Segunda imagem.
        combined_image (np.array): Imagem combinada.
    """
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    axis[0].imshow(image1)
    axis[0].set_title('Image 1')
    axis[0].axis('off')

    axis[1].imshow(image2)
    axis[1].set_title('Image 2')
    axis[1].axis('off')

    axis[2].imshow(combined_image)
    axis[2].set_title('Combined Image')
    axis[2].axis('off')

    plt.tight_layout()
    plt.show()
