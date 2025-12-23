from app import create_app, db

app = create_app()

# Initialize database tables on startup
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print(f"Database initialization error: {e}")

if __name__ == '__main__':
    app.run(debug=False)