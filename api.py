from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from selenium import webdriver
from selenium.webdriver.common.by import By
from pydantic import BaseModel
from typing import List

# FastAPI app instance
app = FastAPI()

# CORS settings to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Model for the request body
class ScrapeRequest(BaseModel):
    topic: str
    num_projects: int


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

        project_info = []

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

            project_info.append(
                {
                    "Project Name": project_name,
                    "Project Price": project_price,
                    "Project Owner": project_owner,
                    "Rating": rating,
                }
            )

        return project_info

    except Exception as e:
        return {"error": str(e)}

    finally:
        # Close the web driver
        driver.quit()


# API endpoint to scrape project information
@app.post("/scrape-projects/", response_model=List[dict])
async def scrape_projects(request_data: ScrapeRequest):
    topic = request_data.topic
    num_projects = request_data.num_projects
    project_info = scrape_upwork_projects(topic, num_projects)
    return project_info
