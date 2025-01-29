import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import HTMLResponse

app = FastAPI()


# başka işlemler çalışırken bekleme yapmadan download etsin
@app.get("/download")
async def download():
    file_path = "C:/Users/zeyrabilgecartcurt/Desktop/zeyra_workspace/python/basic algorithm/example_1.py"
    return FileResponse(file_path, filename="python örnek", media_type="application/pdf")


html_form = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Dosya İndirme</title>
</head>
<body>
    <button id="downloadBtn">Dosyayı İndir</button>

    <script>
        document.getElementById("downloadBtn").addEventListener("click", function() {
            window.location.href = "/download";
        });
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def home():
    return html_form


if __name__ == "__main__":
    uvicorn.run("download_fast_api:app", host="0.0.0.0", port=8000, reload=True)
