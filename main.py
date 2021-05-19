from website import create_app

app = create_app()

if __name__ == "__main__":
    # the above line means => only when you run this file.. Not when you import this file.
    app.run(debug=True)