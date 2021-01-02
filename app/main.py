from fastapi import FastAPI


app = FastAPI(title='Simple Post app')


@app.get('/')
async def start_page():
    return {}
