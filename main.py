import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By


# Function to scrape project information
def scrape_upwork_projects(topic, num_projects):
    # Construct the URL with the provided topic
    url = f"https://www.upwork.com/services/search?nbs=1&q={topic}"

    # Initialize a web driver (you need to have a compatible driver installed, e.g., ChromeDriver)
    driver = webdriver.Chrome()

    try:
        # Open the URL in the web driver
        driver.get(url)

        # Find elements that contain project information
        project_elements = driver.find_elements(
            By.CLASS_NAME, "project-tile__container"
        )

        # Limit the number of projects to be printed based on the user's input
        num_projects = min(num_projects, len(project_elements))

        for element in project_elements[:num_projects]:
            # Extract project name
            project_name_element = element.find_element(
                By.CLASS_NAME, "project-tile__title"
            )
            project_name = project_name_element.text

            # Extract project price
            project_price_element = element.find_element(By.CLASS_NAME, "price")
            project_price = project_price_element.text

            # Extract project owner
            project_owner_element = element.find_element(
                By.CLASS_NAME, "user-badge__content"
            )
            project_owner = project_owner_element.text

            # Extract rating
            rating_element = element.find_element(By.CLASS_NAME, "user-rating")
            rating = rating_element.text

            print("Project Name:", project_name)
            print("Project Price:", project_price)
            print("Project Owner:", project_owner)
            print("Rating:", rating)
            print()

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the web driver
        driver.quit()


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Upwork Project Scraper")
    parser.add_argument("--topic", type=str, required=True, help="Search topic")
    parser.add_argument("--n", type=int, default=5, help="Number of projects to print")

    args = parser.parse_args()

    # Call the scrape function with the provided arguments
    scrape_upwork_projects(args.topic, args.n)
