# AAS 1100 Mapping/Community Final Project

Our final project for AAS 1100 is to find and explain Asian communities in Ithaca by creating a map of Asian communities in Ithaca using census data. In this repo, we built a web scraping tool to easily and rapidly collect census data from ancestry.com We also built some data visualizations to view interesting trends and clusters in our collected data.

# Process
1. We run a web scraper that collects data from ancestry.com.
2. We clean up the data in a Jupyter Notebook. This includes things like filtering out missing data, combining values like 'Street' and 'House Number' to get a full address, and generating place ids to easily map on GMaps.
3. We visualize the cleaned data on bar graphs, pie charts, and maps.

# How to Run
1. Run `pip install -r requirements.txt` in virutalenv.
2. Run `python3 collection/scraper.py` to collect data. View output in `output/people.csv`.
3. Run the Jupyter Notebook in `cleaning` to generate place ids. View output in `output/place_ids.csv`.
4. Run `python3 -m http.server --directory visualization` to run the map viz.
Note: You'll need to login into your Cornell account for 2. You'll also need a GMaps Key for 3 (which you can request from me). You should be able to view 4 from Cornell's WiFi networks. If you can't let me know your IP address to add it to the allowlist.
