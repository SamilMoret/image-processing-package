from PIL import Image,ImageFilter,  ImageDraw, ImageFont


def apply_blur(input_path, output_path):
    """
    Aplica um filtro de desfoque à imagem e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem desfocada será salva.
    """
    image = Image.open(input_path)
    blurred_image = image.filter(ImageFilter.BLUR)  # Aplica o filtro de desfoque
    blurred_image.save(output_path)


def resize_image(input_path, output_path, size):
    """
    Redimensiona a imagem para um tamanho específico e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem redimensionada será salva.
        size (tuple): Nova dimensão (largura, altura) da imagem.
    """
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

def apply_grayscale(input_path, output_path):
    """
    Aplica o filtro de escala de cinza à imagem e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem em escala de cinza será salva.
    """
    image = Image.open(input_path).convert("L")  # Converte para escala de cinza
    image.save(output_path)

def rotate_image(input_path, output_path, degrees):
    """
    Rotaciona a imagem por um número de graus especificado e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem rotacionada será salva.
        degrees (int): Número de graus para rotacionar a imagem.
    """
    image = Image.open(input_path)
    rotated_image = image.rotate(degrees)
    rotated_image.save(output_path)

def apply_filter(input_path, output_path, filter_type):
    """
    Aplica um filtro à imagem e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem filtrada será salva.
        filter_type: Filtro a ser aplicado (exemplo: ImageFilter.BLUR).
    """
    image = Image.open(input_path)
    filtered_image = image.filter(filter_type)
    filtered_image.save(output_path)


def add_text(input_path, output_path, text, position):
    """
    Adiciona texto à imagem e salva o resultado.

    Args:
        input_path (str): Caminho da imagem de entrada.
        output_path (str): Caminho onde a imagem com texto será salva.
        text (str): Texto a ser adicionado.
        position (tuple): Posição onde o texto será adicionado (x, y).
    """
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Use a fonte padrão
    draw.text(position, text, (255, 255, 255), font=font)  # Texto em branco
    image.save(output_path)

