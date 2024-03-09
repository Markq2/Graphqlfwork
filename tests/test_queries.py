import pytest
from utilities.graphql_requests import GraphQLRequests
from utilities.data_parser import DataParser
from utilities.logger import Logger

class TestGraphQLQueries:
    logger = Logger.setup_logger()

    @pytest.mark.parametrize("country_code", ["BR", "CA", "AU"])
    def test_get_country_info(self, country_code):
        query = """
        query GetCountry {
          country(code: "%s") {
            name
            native
            capital
            emoji
            currency
            languages {
              code
              name
            }
          }
        }
        """ % country_code

        parsed_response = DataParser.parse_json(GraphQLRequests.send_graphql_request(query))

        self.logger.info(f"Response for {country_code}: {parsed_response}")
        print(parsed_response)