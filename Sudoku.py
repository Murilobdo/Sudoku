import cv2 as cv

for i in range(8):
    #abrindo a imagem e setando um tamanho
    _ = cv.imread("img/sudoku{}.jpg".format(i + 1), cv.IMREAD_GRAYSCALE)
    img = cv.resize(_, (512,512))

    #aplicando um filtro
    kernelSizeMedianBlur = 5
    medianBlur = cv.medianBlur(img,kernelSizeMedianBlur)

    #binarizando a imagem
    (_, binaryImage) = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
    (_, binaryImage) = cv.threshold(binaryImage, 127, 255, 0)

    #pegando os contornos
    contours, hierarchy = cv.findContours(binaryImage, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    
    #desenhando os retangulos dos contornos
    for _ in zip(contours, hierarchy):
        _contour = _[0]
        _hierarchy = _[1]
        #[Next, Previous, First_Child, Parent]
        if(_hierarchy[3] <= 0 and _hierarchy[0] > -1):
            (x,y,w,h) = cv.boundingRect(_contour)
            cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    
    cv.imshow("Imagem {}".format(i + 1), img)
    cv.waitKey()
cv.waitKey()
