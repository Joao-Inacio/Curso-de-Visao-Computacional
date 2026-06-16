import cv2
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

caminho_imagem = BASE_DIR / "data" / "imagem.jpg"

imagem = cv2.imread(str(caminho_imagem))

cv2.imshow('Primeira Imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(imagem.shape)
