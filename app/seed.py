from app import app, db
from app.models import Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    ]

    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super senses", description="allows the wielder to use her senses at a super-human level"),
    ]

    db.session.add_all(heroes + powers)
    db.session.commit()

    links = [
        HeroPower(hero_id=1, power_id=2, strength="Strong"),
        HeroPower(hero_id=2, power_id=1, strength="Average"),
    ]

    db.session.add_all(links)
    db.session.commit()

    print("🌱 DB seeded successfully!")
