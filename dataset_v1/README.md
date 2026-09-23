# DrainGuard Dataset v1 - auto debris draft

Classes:
- 0: drain
- 1: debris

Conversion rules:
- source `storm_drain_inlet` -> `drain`
- source `leaves` polygon -> `drain`; debris masks are AUTO-GENERATED from pixels inside the source polygon
- source `manhole_cover` -> negative/background sample (empty label)

Statistics:
{'images': 451, 'drain_imgs': 300, 'negative_imgs': 150, 'debris_imgs': 147, 'debris_polys': 1021}

IMPORTANT: `debris` is pseudo-labeling, not manually verified ground truth. Review the 150 source-leaves images before treating this as final training data. `AUTO_DEBRIS_REVIEW.csv` lists them.
