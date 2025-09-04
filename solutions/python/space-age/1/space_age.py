class SpaceAge:
    def __init__(self, seconds):
        self.orbital_periods = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132
}
        self.seconds = seconds
        self.years = seconds / (60*60*24*365.25)
    
        for planet, conversion in self.orbital_periods.items():
            func = lambda self, current=conversion: round(self.years / current, 2)
            setattr(self, f"on_{planet}", func.__get__(self))

