def sanitize_json_string(json_string):
    # Remover delimitadores o caracteres no deseados
    cleaned = json_string.replace('```json', '').replace('```', '')
    
    # Remover espacios innecesarios
    cleaned = cleaned.strip()
    
    return cleaned