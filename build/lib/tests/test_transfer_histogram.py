import os
import numpy as np
import matplotlib.pyplot as plt
from processing.combination import transfer_histogram

def compute_histogram(image):
    """Computa o histograma para cada canal de uma imagem RGB."""
    if image.ndim == 3:  # Se a imagem é colorida (RGB)
        # Obtemos o histograma para cada canal
        histograms = [np.histogram(image[:, :, i], bins=256)[0] for i in range(image.shape[2])]
        return histograms
    else:  # Se a imagem é em escala de cinza
        return np.histogram(image, bins=256)[0]

def test_transfer_histogram():
    # Caminho das novas imagens
    current_dir = os.path.dirname(__file__)
    image3_path = os.path.join(current_dir, 'imagem_teste', 'image3.jpg')
    image4_path = os.path.join(current_dir, 'imagem_teste', 'image4.jpg')

    # Carregar as novas imagens
    image3 = plt.imread(image3_path)
    image4 = plt.imread(image4_path)

    # Realizar a transferência de histograma
    matched_image = transfer_histogram(image3, image4)

    # Obter os histogramas de ambas as imagens antes e depois
    hist_image3 = compute_histogram(image3)
    hist_image4 = compute_histogram(image4)
    hist_matched = compute_histogram(matched_image)

    # Calcular a diferença antes e depois da transferência em todos os canais (R, G, B)
    diff_before = sum([np.sum(np.abs(hist_image3[i] - hist_image4[i])) for i in range(3)])  # Comparação em todos os canais
    diff_after = sum([np.sum(np.abs(hist_image3[i] - hist_matched[i])) for i in range(3)])  # Comparação em todos os canais

    # Imprimir as diferenças para diagnóstico
    print(f"Diferença antes da transferência (todos os canais): {diff_before}")
    print(f"Diferença após a transferência (todos os canais): {diff_after}")

    # Certifique-se de que a diferença após a transferência do histograma é menor
    assert diff_after < diff_before, "O histograma ajustado não corresponde à primeira imagem"
