from flask import Blueprint, jsonify, request

class Planet:
    def __init__(self, id, name, description, order_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.order_from_sun = order_from_sun

planet1 = Planet(1, "Mercury", 
"A small planet with a rocky surface and little atmosphere.", "closest to the sun")

planet2 = Planet(2, "Venus",
"A hot, lovely world with thick, toxic clouds.", "second from the sun")

planet3 = Planet(3, "Earth", 
"Our blue-green home, filled with life and wonder.", "third from the sun")

planet4 = Planet(4, "Mars", 
"The red planet, thin atmosphere and massive dust storms.", "fourth from the sun")

planet5 = Planet(5, "Jupiter",
"A gas giant with a big red spot and many moons.", "fifth from the sun")

planet6 = Planet(6, "Saturn",
"The iconic planet with stunning rings and numerous moons.", "sixth from the sun")

planet7 = Planet(7, "Uranus", 
"An icy gas giant with an unusual tilt and faint rings.", "seventh from the sun")

planet8 = Planet(8, "Neptune", 
"A distant, windy world with the fastest winds in the solar system.", "eighth from the sun")

planets = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planets:
        planet_dict = {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description, 
        "order_from_sun": planet.order_from_sun }

        response.append(planet_dict)

    return jsonify(response), 200

@planets_bp.route("/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    if planet_id <= 0:
        return jsonify({"error": "Invalid planet_id"}), 400

    planet_found = None
    for planet in planets:
        if planet.id == planet_id:
            planet_found = planet
            break

    if planet_found is None:
        return jsonify({"error": "Planet not found"}), 404

    planet_dict = {
        "id": planet_found.id,
        "name": planet_found.name,
        "description": planet_found.description,
        "order_from_sun": planet_found.order_from_sun
    }

    return jsonify(planet_dict), 200
