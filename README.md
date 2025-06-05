Prova - Visão computacional 

1- Pré processar ao menos 6 imagens de 2 animais diferentes aplicando redimensionamento, filtro Gaussiano e Equalização de histograma. 
Depois fazer a classificação com IA destas imagens processadas, separando o conjunto em 80% para treino e 20% teste para ver se a IA conseguiria fazer a classificação correta, e por fim mostrar as metricas de avaliação e desempenho da IA. 

2- O opencv foi usado para carregar as imagens e fazer o pré processamento. No pré processamento foram utilizadas as ferramentas de redimensionamento, desfoque, cinza (apliquei o cinza para aparecer melhor a equalização ja que a grande maioria das imagens nao tinha tanto cinza) e equalização de histograma. Usei o scv kernel porque como seria a classificação de dois tipos diferentes ele se sai bem com classificação binaria precessadas dessa forma. 

Etapas realizadas: 

 Carregamento de todas as imagens da pasta 'imagens' contendo arquivos como 'gato1.jpeg' e `cachorro.jpeg'.
 Pré-processamento de cada imagem na tela: Redimensionamento para 128x128, aplicação de filtro Gaussiano, conversão para tons de cinza equalização de histograma,visualização de todas as etapas para cada imagem.
Divisão dos dados em treino (80%) e teste (20%), treinamento do modelo SVM e avaliação com métricas: precisão, recall e F1-score.


Resultados obtidos:

 precision    recall  f1-score   support

    cachorro       0.00      0.00      0.00         1
        gato       0.67      1.00      0.80         2

        gato       0.67      1.00      0.80         2


    accuracy                           0.67         3
    accuracy                           0.67         3
   macro avg       0.33      0.50      0.40         3
weighted avg       0.44      0.67      0.53         3

Tempo total gasto: 1h 40m


Dificuldaed encontrada: fazer o pre processamento de variais imagens aparecerem na tela após o termino da ultima.