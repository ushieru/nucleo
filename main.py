from src import app

if __name__ == '__main__':
    # Add host='0.0.0.0' to set visible
    app.run(port=3000, debug=True)