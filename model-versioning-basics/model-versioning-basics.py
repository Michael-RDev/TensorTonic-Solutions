def promote_model(models: list) -> str:
    if not models:
        return ""

    best_model = max(models, key=lambda m: (m["accuracy"], -m["latency"], m["timestamp"]))
    return best_model["name"]