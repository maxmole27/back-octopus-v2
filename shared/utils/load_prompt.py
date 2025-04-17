def load_prompt(ruta: str) -> str:
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()