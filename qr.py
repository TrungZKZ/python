import cv2 as cv
from pyzbar import pyzbar
import time



cap = cv.VideoCapture(0)

barcode_count = 0
barcodeData_prv = ""
barcode_coordinates = ""


while True:
    
    if cv.waitKey(1) == ord('q'):
        break

    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)

    if not barcodes:
        cv.putText(frame, "No any Barcode Detected", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    else:
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = "{}".format(barcodeData, barcodeType)
            cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            if barcodeData_prv != barcodeData:
                barcode_count += 1
                barcodeData_prv = barcodeData
                barcode_coordinates = "Coordinates: X={}, Y={}".format(x, y)

            cv.putText(frame, barcode_coordinates, (x - 10, y - 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv.putText(frame, barcodeData, (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            cv.putText(frame, barcode_coordinates, (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cv.putText(frame, current_time, (10, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv.putText(frame, str(barcode_count), (10, 80), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv.putText(frame, barcode_coordinates, (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv.imshow('video', frame)
cap.release()
cv.destroyAllWindows()
