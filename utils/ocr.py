from rapidocr_onnxruntime import RapidOCR

from exceptions.OCRException import OCRException


class OCRHelper:
    def __init__(self):
        self._ocr_engine = RapidOCR()
        self._ocr_images = []

    @property
    def get_ocr_engine(self):
        if self._ocr_engine is None:
            self._ocr_engine = RapidOCR()
        return self._ocr_engine


class OCR:
    def __init__(self, image_path, ocr_helper, *, use_det=True, use_cls=False, use_rec=True):
        self._image_path = image_path
        self._result, self._elapse = ocr_helper.get_ocr_engine(self._image_path, use_det=use_det, use_cls=use_cls, use_rec=use_rec)

    @property
    def get_results(self):
        if self._result is None:
            raise OCRException("Image {} get context failed.".format(self._image_path))
        return self._result
