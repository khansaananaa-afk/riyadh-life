# Sources and licensing

| Source | Intended use | Notes |
|---|---|---|
| Riyadh Municipality GIS Portal — https://alriyadh.gov.sa/en/new/gis-portal | Official layers, neighborhoods, streets, public facilities, potential exportable GIS layers | Check portal terms and export permissions. |
| Riyadh Municipality Open Data — https://alriyadh.gov.sa/en/new/open-data | Government datasets | Dataset-specific licenses and terms apply. |
| RCRC Open Data Portal — https://opendata.rcrc.gov.sa/ | Roads and traffic, metro/bus, land/urban indicators, heritage, commercial/entertainment datasets | Check each dataset's license and format. |
| Saudi National Geospatial Platform — https://my.gov.sa/en/content/gis | National geospatial layers | Registration/access may be required; check dataset terms. |
| OpenStreetMap — https://www.openstreetmap.org/ | Roads, building footprints, amenities, land use, mapped POIs | ODbL 1.0; attribution required. See https://www.openstreetmap.org/copyright |
| Overpass API — https://overpass-api.de/ | Query OSM features for the game area | Public service; use politely and respect rate limits. |
| BBBike Extract — https://extract.bbbike.org/ | Alternative custom-area OSM extracts in GeoJSON, PBF, GeoPackage, etc. | OSM-derived data; ODbL attribution applies. |

## Landmark coordinate references

- Kingdom Centre: Mapcarta/OpenStreetMap-derived reference — https://mapcarta.com/W264745922
- Al Faisaliah Tower: published coordinates — https://en.wikipedia.org/wiki/Al_Faisaliah_Tower
- KAFD World Trade Center: published coordinates — https://en.wikipedia.org/wiki/KAFD_World_Trade_Center
- At-Turaif: UNESCO nomination document — https://whc.unesco.org/document/168966
- Boulevard Riyadh City: reference location shown in an ANB active-locations PDF — https://anb.com.sa/documents/55607/0/anb%2BAll%2BActive%2BLocations2fff.pdf/d8bb8190-7674-8cc1-d151-3be28353a42d?t=1756906026169

Coordinates in `riyadh_landmarks.geojson` are reference points only. Validate them against official GIS or current OSM geometry before final placement.

## OSM attribution

If using OpenStreetMap-derived data, credit:
"© OpenStreetMap contributors"

Include a link to https://www.openstreetmap.org/copyright and comply with ODbL 1.0. Review whether your combined/derived database triggers share-alike obligations.
