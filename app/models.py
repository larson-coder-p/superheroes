from sqlalchemy.orm import validates
from . import db

# Represents a superhero with a real name and a super name
class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)  # unique identifier
    name = db.Column(db.String, nullable=False)   # actual name of the hero
    super_name = db.Column(db.String, nullable=False)  # superhero nickname

    # Relationship: One hero can have many hero powers
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    # Serialization
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }

#
# Represents a superpower
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)  # unique ID
    name = db.Column(db.String, nullable=False)   # name of the power
    description = db.Column(db.String, nullable=False)  # what the power does

    # Relationship: One power can be used by many heroes
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    # Validation
    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }



class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)  # Strength level of power: Weak, Average, Strong

    # Foreign Keys
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)  # references Hero
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)  # references Power

    # Validation
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Average', 'Weak']:
            raise ValueError("Strength must be one of: 'Strong', 'Average', 'Weak'")
        return value

    # Serialize HeroPower
    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "power": self.power.to_dict()  
        }
