from PIL import Image

# Cria duas imagens de teste
def create_test_images():
    image1 = Image.new('RGB', (100, 100), color = 'red')
    image1.save("test_image1.jpg")

    image2 = Image.new('RGB', (100, 100), color = 'blue')
    image2.save("test_image2.jpg")

create_test_images()
