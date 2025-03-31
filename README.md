# superheroes
  This is a Flask RESTful API for managing a database of heroes, their powers, and the strengths of those powers via a join table.


##  Features

- View all heroes
- View individual hero + their powers
- View and update superpowers
- Associate heroes with powers (with strength)
- Validations for clean, safe data
- Fully RESTful routing
- JSON responses with nested structure

##  Setup Instructions

### 1. Clone this repo & navigate to the folder

```bash
git clone git@github.com:larson-coder-p/superheroes.git
cd superheroes

2. Create virtual environment & activate it
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Migrate the database
bash
Copy
Edit
flask db init
flask db migrate -m "initial"
flask db upgrade

5. Seed the database
bash
Copy
Edit
python -m app.seed

6. Run the server
bash
Copy
Edit
python run.py
Open Postman or browser:
 http://127.0.0.1:5000/

🔌 API Endpoints
GET /heroes
Returns all heroes:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
GET /heroes/<id>
Returns a hero with their powers:

json
Copy
Edit
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "strength": "Strong",
      "hero_id": 1,
      "power_id": 2,
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed"
      }
    }
  ]
}
If not found:

json
Copy
Edit
{
  "error": "Hero not found"
}
GET /powers
Returns all powers.

GET /powers/<id>
Returns one power or:

json
Copy
Edit
{
  "error": "Power not found"
}
PATCH /powers/<id>
Update description:

json
Copy
Edit
{
  "description": "Updated description longer than 20 characters"
}
Errors:

json
Copy
Edit
{ "errors": ["Description must be at least 20 characters long."] }
POST /hero_powers
Create a new HeroPower:

json
Copy
Edit
{
  "strength": "Average",
  "hero_id": 3,
  "power_id": 1
}
Success:

json
Copy
Edit
{
  "id": 10,
  "strength": "Average",
  "hero_id": 3,
  "power_id": 1,
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
Errors:

json
Copy
Edit
{ "errors": ["Strength must be one of: 'Strong', 'Average', 'Weak'"] }

Testing With Postman
Open Postman

Import the collection file if provided:
challenge-2-superheroes.postman_collection.json

Send requests to:
http://127.0.0.1:5000

Validations
Field	Validation
Power.description	Required, min 20 characters
HeroPower.strength	Must be "Strong", "Average", "Weak"

Tech Stack
Python 3.8+

Flask

Flask-SQLAlchemy

Flask-Migrate

SQLite3

 Author
Built by Larson Gitonga as part of Flatiron School Phase 4 Challenge 