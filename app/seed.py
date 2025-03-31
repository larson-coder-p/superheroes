# Seeder script to populate the database with sample data

from app import app, db
from app.models import Hero, Power, HeroPower

# Run seeding inside Flask app context
with app.app_context():
    db.drop_all()   # Remove all existing tables/data
    db.create_all() # Recreate tables based on models

    # Add sample heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    ]

    # Add sample powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super senses", description="allows the wielder to use her senses at a super-human level"),
    ]

    # Commit heroes and powers to the DB
    db.session.add_all(heroes + powers)
    db.session.commit()

    # Associate heroes with powers using HeroPower join table
    links = [
        HeroPower(hero_id=1, power_id=2, strength="Strong"),
        HeroPower(hero_id=2, power_id=1, strength="Average"),
    ]

    db.session.add_all(links)
    db.session.commit()

    print("🌱 Database seeded successfully!")
