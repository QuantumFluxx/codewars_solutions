object GetPlanetName {
    final val planet_names = Array(
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto"
    )

    def get_planet_name(id: Int): String = planet_names(id - 1)
}
