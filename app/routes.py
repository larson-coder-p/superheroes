from flask import Blueprint, jsonify, request
from .models import Hero, Power, HeroPower
from . import db

# Create a blueprint for the API routes
api_bp = Blueprint('api', __name__)

# Root route – quick check to confirm API is running
@api_bp.route('/')
def index():
    return jsonify({"message": "Superhero API is alive!"}), 200


# Return all heroes as a list of dictionaries
@api_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200


# Return one hero, along with their powers
@api_bp.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        **hero.to_dict(),
        "hero_powers": [hp.to_dict() for hp in hero.hero_powers]
    }), 200

# Return all powers
@api_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


# Return a specific power by ID
@api_bp.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200


# Update a power's description
@api_bp.route('/powers/<int:power_id>', methods=['PATCH'])
def patch_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400


# Create a new association between a hero and a power
@api_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()

        # Return nested response showing both hero and power
        return jsonify({
            "id": hero_power.id,
            "strength": hero_power.strength,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "hero": hero_power.hero.to_dict(),
            "power": hero_power.power.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
