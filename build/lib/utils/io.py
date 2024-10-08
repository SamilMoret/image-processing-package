from PIL import Image

def load_image(image_path):
    """
    Carrega uma imagem a partir de um caminho.
    """
    return Image.open(image_path)

def save_image(image, output_path):
    """
    Salva uma imagem em um caminho especificado.
    """
    image.save(output_path)
