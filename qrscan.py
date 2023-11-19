if __name__ == '__main__':

    import cv2 as cv
    import os

    try:
        from pyzbar.pyzbar import decode, ZBarSymbol
    except:
        cmd = ('py -m pip install "pyzbar"')
        os.system(cmd)
        from pyzbar.pyzbar import decode, ZBarSymbol

    def capt(debug=False, img=True):

        for i in range(3):
            cap = cv.VideoCapture("Camera2.mp4")
            ret, frame = cap.read()
            cv.imshow('frame', frame)
        if img == True:
            return(decode(cv.imread(frame)))
        else:
            return(decode(frame))

    def capt2(cap, debug=False, img=True):
            ret, frame = cap.read()
            cv.imshow('frame', frame)
            if img == True:
                cv.imwrite('imgs.png', frame)
                return(decode(frame))

            else:
                return(decode(frame))



    # 1 интерация
    b = []


    # 2 интерация
    cap = cv.VideoCapture("Camera2.mp4")
    info = capt2(cap)
    while True:
        a = []

        for i in info:
            data = i.data.decode("utf-8")
            a.append(data)
        for i in range(max(len(a), len(b))): #перебор массивов
            try:
                if b[i] not in a:
                    b.remove(b[i])
                    print(b)
                    #обновляем статус b[i] qr в бд
                    # post_http_request (url, b)
                    # post_http_request('http://127.0.0.1:8001/change_pallet_status', {
                    #     'id_pallet': id_pallet,
                    #     'product_name': 'aasddas',
                    #     'product_batch': '1221',
                    #     'thing_quantity': 12,
                    #     'data_of_manufacture': '2023-11-18',
                    #     'expiration_date': '2023-12-18',
                    #     'api_common_key': signature.get('api_common_key'),
                    #     'signature': signature.get('signature'),
                    #     'timestamp': signature.get('timestamp')
                    # }))
            except:
                pass
            try:
                if a[i] not in b:
                    b.append(a[i])
                    postHttp(url, b)
                    #обновляем статус a[i] qr в бд
            except:
                pass
        info = capt2(cap)

