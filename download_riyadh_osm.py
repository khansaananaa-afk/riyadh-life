#!/usr/bin/env python3
"""
Download starter OpenStreetMap geometry for a broad Riyadh working extent.
Outputs GeoJSON files for roads, building footprints, and selected places/land use.

IMPORTANT:
- The bounding box below is a broad working rectangle, NOT an official city boundary.
- Replace/clip it using an official Riyadh municipal boundary if one is legally downloadable.
- OSM is community-mapped and may be incomplete or uneven in detail.
- Respect ODbL attribution and Overpass fair-use limits.
"""
import json, time, sys
from pathlib import Path
import requests

# south, west, north, east (WGS84)
SOUTH, WEST, NORTH, EAST = 24.30, 46.30, 25.10, 47.20
GRID_ROWS, GRID_COLS = 4, 4
ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]
OUT = Path(__file__).resolve().parents[1] / "data" / "osm_downloads"
OUT.mkdir(parents=True, exist_ok=True)

def tiles():
    dlat = (NORTH-SOUTH)/GRID_ROWS
    dlon = (EAST-WEST)/GRID_COLS
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            s = SOUTH + r*dlat
            n = s + dlat
            w = WEST + c*dlon
            e = w + dlon
            yield s,w,n,e

def query_for(box, kind):
    s,w,n,e = box
    bbox = f"{s},{w},{n},{e}"
    if kind == "roads":
        selector = f'way["highway"]({bbox});'
    elif kind == "buildings":
        selector = f'way["building"]({bbox});'
    else:
        selector = (
            f'way["amenity"]({bbox});'
            f'way["leisure"]({bbox});'
            f'way["landuse"]({bbox});'
            f'way["tourism"]({bbox});'
            f'way["railway"]({bbox});'
        )
    return f'[out:json][timeout:180];({selector});out tags geom;'

def to_features(osm, kind):
    features = []
    for el in osm.get("elements", []):
        if el.get("type") != "way" or not el.get("geometry"):
            continue
        coords = [[p["lon"], p["lat"]] for p in el["geometry"]]
        if len(coords) < 2:
            continue
        closed = coords[0] == coords[-1]
        is_area = closed and len(coords) >= 4 and kind != "roads"
        geom = {"type": "Polygon", "coordinates": [coords]} if is_area else {"type": "LineString", "coordinates": coords}
        features.append({
            "type":"Feature",
            "id":f"osm-way-{el['id']}",
            "properties":{"osm_id":el["id"], "osm_type":"way", **el.get("tags", {})},
            "geometry":geom
        })
    return features

def fetch(session, query):
    last = None
    for endpoint in ENDPOINTS:
        try:
            response = session.post(endpoint, data={"data":query}, timeout=240)
            response.raise_for_status()
            return response.json()
        except Exception as exc:
            last = exc
            time.sleep(3)
    raise RuntimeError(f"All Overpass endpoints failed: {last}")

def main():
    session = requests.Session()
    session.headers.update({"User-Agent":"RiyadhLife-GeoDataStarter/1.0 (educational game development)"})
    combined = {k:[] for k in ("roads","buildings","places")}
    boxes = list(tiles())
    for idx, box in enumerate(boxes, 1):
        print(f"Tile {idx}/{len(boxes)}: {box}")
        for kind in combined:
            try:
                data = fetch(session, query_for(box, kind))
                combined[kind].extend(to_features(data, kind))
                print(f"  {kind}: {len(data.get('elements', []))} OSM ways")
            except Exception as exc:
                print(f"  WARNING: {kind} tile failed: {exc}", file=sys.stderr)
        time.sleep(2.5)  # be polite to public Overpass servers

    for kind, features in combined.items():
        # Deduplicate ways appearing on tile borders
        unique = {f["id"]: f for f in features}
        fc = {"type":"FeatureCollection","name":f"riyadh_osm_{kind}","features":list(unique.values())}
        (OUT / f"riyadh_{kind}.geojson").write_text(json.dumps(fc, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote {OUT / f'riyadh_{kind}.geojson'} ({len(unique)} features)")

    print("\nAttribution required: © OpenStreetMap contributors — https://www.openstreetmap.org/copyright")
    print("Review ODbL obligations and validate the extent/coverage before shipping.")

if __name__ == "__main__":
    main()
