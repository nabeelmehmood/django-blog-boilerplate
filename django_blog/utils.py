import uuid

def get_filename(filename, request):
    ext = filename.split('.')[-1]
    return str(uuid.uuid4())+'.'+ext