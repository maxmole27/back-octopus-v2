import re


def sanitize_filename(filename: str) -> str:
    # Reemplaza los espacios por guiones bajos
    filename = filename.replace(" ", "_")
    
    # Elimina los caracteres que no son alfanuméricos ni permitidos en nombres de archivo
    filename = re.sub(r'[^\w\.-]', '', filename)
    
    # Limita la longitud del nombre si es necesario
    max_length = 255
    return filename[:max_length]