class Mappings:

    _game_phases: list[str] = ["Distribution Platform", "Construction Dock", "Main Body", "Propulsion", "Assembly"]

    _schematics: list[list[str]] = [
        ["Base Building", "Logistics", "Field Research"],
        ["Part Assembly", "Obstacle Clearing", "Jump Pads", "", "Resource Sink Bonus Program"],
        ["Coal Power", "Logistics Mk.2", "Vehicular Transport", "Basic Steel Production"],
        ["Advanced Steel Production", "Enhanced Asset Security", "Expanded Power Infrastructure", "Hypertubes", "FICSIT Blueprints"],
        ["Oil Processing", "Industrial Manufacturing", "Logistics Mk.3", "Fluid Packaging", "Petroleum Power"],
        ["Logistics Mk.4", "Jetpack", "Monorail Train Technology", "", "Pipeline Engineering Mk.2", "FICSIT Blueprints Mk.2", "Railway Signalling"],
        ["Bauxite Refinement", "Logistics Mk.5", "Hazmat Suit", "Aeronautical Engineering", "Control System Development"],
        ["Nuclear Power", "Advanced Aluminum Production", "Hoverpack", "Leading-Edge Production", "Particle Enrichment"],
        ["Matter Conversion", "Quantum Encoding", "FICSIT Blueprints Mk.3", "Spatial Energy Regulation", "Peak Efficiency"]
    ]

    def game_phase(self, phase: str) -> str:
        return self._game_phases[int(phase[-2]) - 1]

    def schematic(self, schematic: str) -> str:
        return self._schematics[int(schematic[-6]) - 1][int(schematic[-4]) - 1]