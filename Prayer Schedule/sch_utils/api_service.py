import requests


def get_schedule(self):

    city = self.city_input.text()
    country = self.country_input.text()

    if not city or not country:
        self.location_label.setText("Please fill in the text.")
        return

   
    url = f"http://api.aladhan.com/v1/timingsByCity/11-11-2025?city={city}&country={country}&method=20"

    try:
        response = requests.get(url, timeout=10)  # Tambahkan timeout biar aman
        response.raise_for_status()
        data = response.json()

        if data["code"] == 200:
            timings = data['data']['timings']

            
            self.display_schedule(data)
            self.get_active_prayer(timings)

            location_label = f"{city}, {country}"
            self.location_label.setText(location_label)
        else:
            self.location_label.setText(
                f"Location of {city} City and {country} Country not found")

    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                self.display_error('Bad Requests:\nPlease Check Your Input')
            case 403:
                self.display_error("Forbidden:\nAcces is denied")
            case 500:
                self.display_error(
                    "Internal Server Error:\nPlease Try Again Later")
            case 502:
                self.display_error(
                    "Bad Gateway:\nInvalid response from the server")
            case 503:
                self.display_error("Service Unavailable:\nServer id down")
            case 504:
                self.display_error(
                    "Gateway Timeout:\nNo response from the server")
            case _:
                self.display_error(f"HTTP error occured:\n{http_error}")

    except requests.exceptions.ConnectionError:
        self.display_error(
            "Connection Error:\n Check your internet connection")

    except requests.exceptions.Timeout:
        self.display_error("Timeout Error:\nThe requests timed out")

    except requests.exceptions.TooManyRedirects:
        self.display_error("Too many Redirects:\n Check the URL")

    except requests.exceptions.RequestException as req_error:
        self.display_error(f"Request Error:\n{req_error}")

    self.city_input.show()
    self.country_input.hide()
    self.city_input.clear()
    self.country_input.clear()
