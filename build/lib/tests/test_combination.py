from processing.combination import combine_images
import os

def test_combine_images():
    # Defina os caminhos para as imagens de teste e o arquivo de saída
    image1_path = "test_image1.jpg"
    image2_path = "test_image2.jpg"
    output_path = "combined_image.jpg"
    
    # Chame a função com os três argumentos necessários
    combine_images(image1_path, image2_path, output_path)
    
    # Verifique se o arquivo foi criado
    assert os.path.exists(output_path)
