import requests


def show_weather(locations, config):
	url_template = "https://wttr.in/{}"
	for location in locations:
		url = url_template.format(location)
		response = requests.get(url, params=config)
		response.raise_for_status()
		print(response.text)


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
	show_weather(locations, config)



if __name__ == "__main__":
	main()
