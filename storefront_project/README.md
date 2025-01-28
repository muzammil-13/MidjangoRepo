# E-commerce Storefront Project

A robust Django-based e-commerce platform that provides a seamless shopping experience with essential features for both customers and administrators.

## Features

### Product Management

- Category-based product organization
- Detailed product listings with images
- Stock tracking and availability status
- Advanced product search functionality
- Paginated product display

### Shopping Cart

- Session-based cart system
- Add/remove items
- Quantity management
- Real-time total calculation
- Stock availability checks

### Admin Interface

- User-friendly product management
- Inline editing capabilities
- Automated slug generation
- Stock and price updates
- Category management

## Technical Stack

- Django
- Python
- SQLite Database
- Django Template Engine

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/storefront_project.git
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Start development server:

```bash
python manage.py runserver
```

## Project Structure

```bash
storefront_project/
├── shop/               # Main shop application
├── cart/              # Shopping cart functionality
├── search_app/        # Search functionality
└── media/             # Product and category images
```

## Usage

1. Access admin panel at `/admin` to manage products and categories
2. Browse products by category
3. Use search functionality to find specific products
4. Add products to cart and manage quantities
5. View cart details and proceed to checkout

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
