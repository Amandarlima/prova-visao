import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

def mostrar_imagem(ibagens, bixinho):
    cv2.imshow(ibagens, bixinho)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

caminho_pasta = "imagens"

imagens = []
rotulos = []

for nome_arquivo in os.listdir(caminho_pasta):
    caminho = os.path.join(caminho_pasta, nome_arquivo)

    if "gato" in nome_arquivo.lower():
        rotulo = "gato"
    elif "cachorro" in nome_arquivo.lower():
        rotulo = "cachorro"
    else:
        continue  
  
    img = cv2.imread(caminho)
    if img is None:
        continue

    mostrar_imagem(f"Original - {nome_arquivo}", img)

    img_red = cv2.resize(img, (128, 128))
    mostrar_imagem(f"Redimensionada - {nome_arquivo}", img_red)

    img_blur = cv2.GaussianBlur(img_red, (3, 3), 1)
    mostrar_imagem(f"Desfocada - {nome_arquivo}", img_blur)

    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    mostrar_imagem(f"Cinza - {nome_arquivo}", img_gray)

    img_eq = cv2.equalizeHist(img_gray)
    mostrar_imagem(f"Equalizada - {nome_arquivo}", img_eq)


    imagens.append(img_eq.flatten())
    rotulos.append(rotulo)

X = np.array(imagens)
y = LabelEncoder().fit_transform(rotulos)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

modelo = SVC(kernel='linear')
modelo.fit(X_train, y_train)


y_pred = modelo.predict(X_test)
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=["cachorro", "gato"]))
