import numpy as np

def create_combined_image(image1, image2):
    """
    Combina duas imagens, gerando uma nova imagem que representa a média das cores.
    
    Args:
        image1 (np.array): Primeira imagem.
        image2 (np.array): Segunda imagem.
        
    Returns:
        np.array: Imagem combinada.
    """
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho")

    # Combina as imagens
    combined = (image1 / 2 + image2 / 2).astype(np.uint8)  # Ajuste para a média das cores
    return combined
