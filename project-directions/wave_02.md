# Wave 02: Read One Book and 404s

## RESTful Endpoint(s): Read One Planet
<!-- Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get one existing `planet`, so that I can see the `id`, `name`, `description`, and other data of the `planet`.
1. ... such that trying to get one non-existing `planet` responds with get a `404` response, so that I know the `planet` resource was not found.
1. ... such that trying to get one `planet` with an invalid `planet_id` responds with get a `400` response, so that I know the `planet_id` was invalid. -->
    
from flask import Blueprint, jsonify, request

class Planet:
    def __init__(self, id, name, description, order_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.order_from_sun = order_from_sun

planet1 = Planet(1, "Earth", "weird", 3)
planet2 = Planet(2, "Mars", "hot", 4)
planet3 = Planet(3, "Venus", "orange", 5)

planets = [planet1, planet2, planet3]

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
