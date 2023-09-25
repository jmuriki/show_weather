import requests


def get_weather(locations, config):
	url_template = "https://wttr.in/{}"
	weather_payload = []
	for location in locations:
		url = url_template.format(location)
		response = requests.get(url, params=config)
		response.raise_for_status()
		weather_payload.append(response.text)
	return weather_payload


def main():
	locations = [
		"Лондон",
		"Москва",
		"Санкт-Петербург",
	]
	config = {
		"n": "",
		"T": "",
		"q": "",
		"M": "",
		"lang": "ru"
	}
	weather_payload = get_weather(locations, config)
	for location_weather in weather_payload:
		print(location_weather)


if __name__ == "__main__":
	main()
