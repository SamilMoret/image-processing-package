# Pacote de Processamento de Imagens

Este projeto permite realizar operações de processamento de imagens como combinar imagens, redimensionar e aplicar filtros, transferir histogramas e calcular diferenças entre imagens.


![Demonstração do Pacote de Processamento de Imagens ](https://github.com/SamilMoret/image-processing-package/blob/main/Image_Processing_vi2.gif)

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Exemplos de Uso](#exemplos-de-uso)
- [Testes](#testes)
- [Contribuição](#contribuição)


## Instalação

Para usar este pacote, você precisará ter o Python e o pip instalados. Siga os passos abaixo para instalar o pacote e suas dependências.

1. Clone o repositório:

   ```bash
   git clone https://github.com/SamilMoret/image-processing-package.git
   cd image-processing-package

   ```
2. Instale as dependências:

   ```bash

    pip install -r requirements.txt

   ```


3. Para instalar o pacote localmente, execute:

```bash

pip install .

```

## Uso

Para usar as funcionalidades deste pacote, você deve importar os módulos necessários. Veja a seção de Exemplos de Uso para mais detalhes.

## Funcionalidades

Combinação de Imagens: Combina duas imagens lado a lado.

Redimensionamento: Redimensiona uma imagem para um tamanho específico.

Aplicação de Filtros: Aplica filtros às imagens, como escala de cinza.

Rotação de Imagem: Rotaciona a imagem por um número de graus especificado.

Plotagem de Imagens: Exibe imagens utilizando matplotlib.

Adição de Texto: Adiciona texto a uma imagem em uma posição específica.

Transferência de Histograma: Transfere o histograma de cores de uma imagem para outra.

Cálculo de Diferenças: Compara duas imagens e destaca as diferenças.

## Exemplos de Uso

## Combinar Imagens

```Python
from processing.combination import combine_images

combine_images("image1.jpg", "image2.jpg", "combined_image.jpg")

```

## Redimensionar Imagem

```python

from processing.transformation import resize_image

resize_image("image1.jpg", "resized_image.jpg", (200, 200))

```

## Aplicar Filtro Preto e Branco

```Python
from processing.transformation import apply_grayscale

apply_grayscale("image1.jpg", "grayscale_image1.jpg")

```

## Rotacionar Imagem

```Python
from processing.transformation import rotate_image

rotate_image("image1.jpg", "rotated_image.jpg", 90)  # Rotaciona 90 graus

```

## Plotar Imagem

```Python
from utils.plot import plot_image

plot_image("image1.jpg")

```
## Adicionar Texto

from processing.transformation import add_text

```python
add_text("image1.jpg", "image_with_text.jpg", "Seu Texto Aqui", (10, 10))

```

## Transferir Histograma

```python

from processing.combination import transfer_histogram

matched_image = transfer_histogram("image1.jpg", "image2.jpg")

```

## Calcular Diferenças

```python

from processing.combination import find_difference

difference_image = find_difference("image1.jpg", "image2.jpg")

```

## Testes
Os testes automatizados são implementados usando pytest. Para rodar os testes:

No diretório raiz do projeto, execute:

```bash

pytest

```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request. Ao contribuir, por favor siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma nova branch (git checkout -b feature-nome-da-sua-feature).
3. Faça suas alterações e commit (git commit -m 'Adicionei uma nova feature').
4. Faça push na branch (git push origin feature-nome-da-sua-feature).
5. Abra um Pull Request.
