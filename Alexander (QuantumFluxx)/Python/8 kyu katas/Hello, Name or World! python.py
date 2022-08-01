def hello(name=""):
    return f"Hello, {name.title()}!" if name or len(name)> 1 else "Hello, World!"