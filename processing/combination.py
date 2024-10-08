import numpy as np
from PIL import Image
from skimage.color import rgb2gray
from skimage.exposure import match_histograms, histogram
from skimage.metrics import structural_similarity


def transfer_histogram(image3, image4):
    """
    Transfere o histograma de cores da primeira imagem para a segunda.

    Args:
        image1 (np.array): A primeira imagem como array NumPy.
        image2 (np.array): A segunda imagem como array NumPy.

    Returns:
        np.array: Segunda imagem com o histograma ajustado para combinar com a primeira.
    """
    matched_image = match_histograms(image3, image4, channel_axis=-1)
    return matched_image

def compute_histogram(image):
    """Computa o histograma para cada canal de uma imagem RGB."""
    if image.ndim == 3:  # Se a imagem é colorida (RGB)
        # Obtemos o histograma para cada canal
        histograms = [histogram(image[:, :, i])[0] for i in range(image.shape[2])]
        return histograms
    else:  # Se a imagem é em escala de cinza
        return histogram(image)[0]

def find_difference(image1, image2):
    """
    Compara duas imagens e retorna uma imagem que destaca as diferenças.
    """
    assert image1.shape == image2.shape, "As duas imagens devem ter o mesmo tamanho."
    
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    data_range = gray_image1.max() - gray_image1.min()
    
    (score, difference_image) = structural_similarity(
        gray_image1, gray_image2, full=True, data_range=data_range
    )
    print(f"Similaridade entre as imagens: {score}")
    
    # Normalizar a imagem da diferença
    denom = np.max(difference_image) - np.min(difference_image)
    if denom == 0:  # Evita divisão por zero
        normalized_difference_image = np.zeros_like(difference_image)
    else:
        normalized_difference_image = (difference_image - np.min(difference_image)) / denom
    
    return normalized_difference_image

def combine_images(image3_path, image4_path, output_path):
    """
    Combina duas imagens lado a lado e salva o resultado em um arquivo.

    Args:
        image1_path (str): Caminho da primeira imagem.
        image2_path (str): Caminho da segunda imagem.
        output_path (str): Caminho para salvar a imagem combinada.
    """
    image3 = Image.open(image3_path)
    image4 = Image.open(image4_path)

    # Verifica a altura máxima das duas imagens
    max_height = max(image3.height, image4.height)
    
    # Cria uma nova imagem com largura combinada e altura máxima
    combined_image = Image.new("RGB", (image3.width + image4.width, max_height))
    
    # Cola as duas imagens
    combined_image.paste(image3, (0, 0))
    combined_image.paste(image4, (image3.width, 0))
    
    combined_image.save(output_path)
