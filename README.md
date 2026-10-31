# RIYADH LIFE
Browser 3D open-world prototype set in real Riyadh (Three.js, no build step). / نموذج لعبة عالم مفتوح في الرياض الحقيقية.

## Status / الحالة
Done: lon/lat to local metres projection, 5 real landmark reference points, character select, walking, driving (arcade physics), 1st/3rd-person cameras, touch + keyboard controls, minimap, IndexedDB autosave, loader for OSM roads/buildings.
Not done: GPS routing, official district boundaries, DEM terrain, traffic/pedestrians, jobs/economy/properties, weather/day-night, audio, Rapier physics/collisions.
Landmark models are rough approximations. No road or building data is invented: without OSM files the game shows a warning.

## Run
1. `pip install requests && python scripts/download_riyadh_osm.py` (writes `data/osm_downloads/`; shrink the bbox in the script first, the default is about 90 km wide).
2. `python -m http.server 8000` then open http://localhost:8000 (or load the GeoJSON files from the in-game menu).

## Deploy
Push to GitHub, then Settings > Pages > Source: GitHub Actions. The workflow deploys on push to `main`.

## Controls
WASD/arrows move, Shift run, Space handbrake, F/E enter/exit car, C camera, M big map, Esc menu.

## Data and licenses
See `SOURCES_AND_LICENSES.md`. (c) OpenStreetMap contributors (ODbL): https://www.openstreetmap.org/copyright. Add your own LICENSE for the code.
