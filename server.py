import modal

app = modal.App()

@app.webhook()
def hello():
    return "Hello world!"