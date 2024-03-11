import pytest
import allure
from utilities.graphql_requests import GraphQLRequests
from utilities.data_parser import DataParser
from utilities.logger import Logger


@allure.feature("GraphQL Queries")
class TestGraphQLQueries:
    logger = Logger.setup_logger()

    @allure.story("Get Country Information")
    @pytest.mark.parametrize("country_code", ["BR", "CA", "AU"])
    def test_get_country_info(self, country_code):
        """Test to get country information."""
        query = f"""
        query GetCountry {{
          country(code: "{country_code}") {{
            name
            native
            capital
            emoji
            currency
            languages {{
              code
              name
            }}
          }}
        }}
        """

        with allure.step(f"Sending GraphQL request for country code: {country_code}"):
            response = GraphQLRequests.send_graphql_request(query)

        with allure.step(f"Parsing and logging response for {country_code}"):
            parsed_response = DataParser.parse_json(response.text)
            self.logger.info(f"Response for {country_code}: {parsed_response}")

        with allure.step(f"Verifying 'data' field in the response for {country_code}"):
            assert 'data' in parsed_response, "Response does not contain 'data' field"

    @allure.story("Get Continent Name by Code")
    @pytest.mark.parametrize("codes", ["SA", "NA", "EU"])
    def test_get_continent_name_by_code(self, codes):
        """Test to get continent name by code."""
        query = f"""
        query GetContinent {{
          continent(code: "{codes}") {{
            name
            countries {{
              code
              name
            }}
          }}
        }}
        """

        with allure.step(f"Sending GraphQL request for continent codes: {codes}"):
            response = GraphQLRequests.send_graphql_request(query)

        with allure.step(f"Parsing and logging response for {codes}"):
            parsed_response = DataParser.parse_json(response.text)
            self.logger.info(f"Response for {codes}: {parsed_response}")

        with allure.step(f"Verifying 'data' field in the response for {codes}"):
            assert 'data' in parsed_response and parsed_response['data'], f"Unexpected response: {parsed_response}"

    @allure.story("Get Countries That Start with 'A'")
    def test_get_countries_starts_with_a(self):
        """Test to get countries that start with the letter 'A'."""
        query = """
        query ListCountriesThatBeginWithTheLetterA {
          countries(filter: { name: { regex: "^A" } }) {
            code
            name
          }
        }
        """

        with allure.step("Sending GraphQL request for countries starting with 'A'"):
            response = GraphQLRequests.send_graphql_request(query)

        with allure.step("Parsing response and verifying country names"):
            parsed_response = DataParser.parse_json(response.text)
            assert all(country['name'].startswith('A') for country in
                       parsed_response.get('data', {}).get('countries', [])), "Not all countries start with 'A'"

    @allure.story("Get Countries with USD Currency")
    def test_get_countries_with_usd_currency(self):
        """Test to get countries that use USD currency."""
        query = """
        query ListCountriesThatUseUSD {
          countries(filter: { currency: { eq: "USD" } }) {
            code
            name
            currency
          }
        }
        """

        with allure.step("Sending GraphQL request for countries using USD currency"):
            response = GraphQLRequests.send_graphql_request(query)

        with allure.step("Parsing and logging response for countries using USD currency"):
            parsed_response = DataParser.parse_json(response.text)
            self.logger.info("Response for countries using USD currency: %s", parsed_response)

        with allure.step("Verifying 'currency' field in the response for countries using USD currency"):
            assert all(country['currency'] == 'USD' for country in
                       parsed_response['data']['countries']), "Not all countries use USD currency"
