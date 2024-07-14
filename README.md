Blog API
This is a RESTful API built using Django, designed to power a personal blog. The API supports basic CRUD operations (Create, Read, Update, Delete) for managing articles.

Features
List Articles: Retrieve a list of all articles
View Article: Retrieve a single article by its ID.
Create Article: Add a new article to the blog.
Delete Article: Remove an article by its ID.
Update Article: Modify an existing article by its ID.
Endpoints
List Articles
URL: /
Method: GET
Query Parameters: Optional filters for date and tags.
View Article
URL: /{id}/
Method: GET
Create Article
URL: /create/
Method: POST
Payload: JSON object with article details (e.g., title, content, tags).
Delete Article
URL: /delete/{id}/
Method: DELETE
Update Article
URL: /update/{id}/
Method: PUT
Payload: JSON object with updated article details.
Getting Started
Prerequisites
Python 3.x
Django 3.x or higher
Django REST Framework
Installation
Clone the repository:
git clone https://github.com/MAYOWA107/blog_api.git

Change into the project directory:
cd blog_api

Install the dependencies:
pip install -r requirements.txt

Apply migrations
python manage.py migrate

Create a superuser (optional, for admin access):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Deployment
The API is deployed and accessible at: https://blog-api-7jbl.onrender.com/p1/

Running Tests
To run tests, execute the following command:
python manage.py test

Contributing
Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or feedback, please contact [ogunkoyamayowa77@gmail.com].
