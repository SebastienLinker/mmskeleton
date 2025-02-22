import lazy_import

pycocotools = lazy_import.lazy_module("pycocotools")
COCO = lazy_import.lazy_module("pycocotools.coco")
COCOeval = lazy_import.lazy_module("pycocotools.cocoeval")
mmdet = lazy_import.lazy_module("mmdet")


def is_exist(module_name):
    module = __import__(module_name)
    try:
        lazy_import._load_module(module)
        return True
    except ImportError:
        return False