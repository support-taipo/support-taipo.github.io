# Map assets and licences

`landsd-logo.jpg` is the unmodified Lands Department logo obtained from the official Map API sample asset at https://api.hkmapservice.gov.hk/mapapi/landsdlogo.jpg on 11 November 2026. It is displayed on the map to meet the public Map API attribution requirement, together with the required map credit. It is not covered by this repository's MIT code licence. [Map API requirements](https://portal.csdi.gov.hk/csdi-webpage/apidoc/TopographicMapAPI).

`leaflet/` contains the unmodified Leaflet 1.9.4 distribution, marker images, source map and its BSD 2-Clause licence. The JS and CSS SHA-256 hashes match the official [Leaflet installation instructions](https://leafletjs.com/install.html). Files were obtained from `https://unpkg.com/leaflet@1.9.4/dist/`; the licence came from the upstream `v1.9.4` tag. Keeping the library on the same site removes the need for a third-party script/CDN request at runtime.
