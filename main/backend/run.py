from app import app
print(__name__)
if __name__ == "__main__":
    app.run(debug=True, port=5001)