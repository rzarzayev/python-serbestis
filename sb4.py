import geoip2.database

# GeoIP verilənlər bazasını yükləmək lazımdır: https://dev.maxmind.com/geoip/geoip2/geolite2/
geoip_db_path = "GeoLite2-City.mmdb"  # GeoLite2 bazası faylı

def get_geo_info(ip_address):
    with geoip2.database.Reader(geoip_db_path) as reader:
        response = reader.city(ip_address)
        return {
            "IP": ip_address,
            "Country": response.country.name,
            "City": response.city.name,
            "Latitude": response.location.latitude,
            "Longitude": response.location.longitude,
        }

# Nümunə IP ünvanını təhlil edin
ip_info = get_geo_info("8.8.8.8")
print(ip_info)
