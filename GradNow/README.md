# GradNow: School Form Management System

A Django-based educational institution form management system designed for efficient student data handling.

## ✨ Features

- Student registration form processing
- Data validation and storage
- Clean administrative interface
- Media file handling
- Static asset management

## 🛠️ Technical Stack

- Django 4.2.5
- Python
- SQLite Database
- Django Templates
- Static/Media Files Support

## 🚀 Project Structure

```bash
GradNow/
├── GradNow/          # Main project settings
├── school/           # Primary application
├── templates/        # HTML templates
├── static/          # Static files
└── media/           # User uploaded content
```

## 🔧 Setup & Installation

1. Clone the repository
2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate virtual environment:

```bash
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start development server:

```bash
python manage.py runserver
```

## 💡 Usage

* Access admin panel at `/admin`
* Main form interface at root URL `/`
* Media files served in debug mode

## 🔐 Environment Configuration

* Debug mode enabled for development
* Configure your own `SECRET_KEY` for production
* Customize `ALLOWED_HOSTS` as needed

## 📦 Dependencies

* Django
* Other requirements listed in requirements.txt

## 🤝 Contributing

Contributions welcome! Feel free to submit pull requests.

## 📝 License

MIT License
