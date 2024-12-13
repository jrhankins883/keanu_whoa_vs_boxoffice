![](https://tenor.com/view/hello-keanu-reeves-spongebob-movie-gif-15554698.gif)
# Does a "Whoa" From Keanu Mean Big Box Office Numbers?

*This is a data analysis project designed to look at the correlation between the box office revenue of Keanu Reeves's films, the number of times he says "Whoa" in those films, and whether it correlates to high or low box office numbers.*

Keanu Reeves has been a movie star since the early 1990's thanks to the *Bill & Ted* movies, *Speed*, *Bram Stoker's Dracula*, the list goes on. Most everyone has seen at least one his movies. Whether you're a fan or not, you've probably heard him utter his signature...

![](https://tenor.com/view/keanu-reeves-whoa-matrix-bro-neo-gif-12028915.gif)

at least once or twice. It's pretty much embedded in pop culture all over the world at this point. As a huge movie buff myself, I get a kick out of hearing him say this one word (like many movie fans do). When I discovered an API containing data that had the number of times he says "whoa" in each of his films, I couldn't believe what I was looking at! I geeked out a little more than I care to admit! While he doesn't say it in every one of his movies, he still has used this signature word over 100 times in the course of his career (118 to be exact).

My initial project idea was far too advanced for my skills at this point in my life so I figured I'd have some fun with this API, indulge my inner movie geek, and find out if a high number of "Whoas" from Keanu will equal a big box office success (as he has had many in his career). Let's find out!

# Data Sources

API:
- [The Movie Database API Website: I got the box office revenue for his films from here](https://api.themoviedb.org)
- [The Keanu Reeves Whoa API](https://whoa.onrender.com/)

# Instructions to Run the Project

This project was developed as a Jupyter Notebook within a virtual environment (new_env) in Visual Studio Code. The main project file, keanu_tmdb.ipynb, can be executed by following these steps:

## Prerequisites

Before getting started, make sure the following requirements are met:

- Python Installed: This project was created using Python 3.12.8. If Python is not installed or you need to update to the latest version, download it from the official [Python website](https://www.python.org/).
- Virtual Environment: Make sure a virtual environment is set up (instructions provided below).
- Git Installed: Git is required to clone the repository. If it’s not already installed, you can find the download on the official [Git website](https://git-scm.com/).

### Setting up the API Key
This project requires an API key from The Movie Database (TMDb) to fetch movie data. Follow the steps below to get your API key and set it up:

1. Sign Up for TMDb:
- Go to [TMDb API Signup Page](https://api.themoviedb.org).
- Create a free account and verify your email address.

2. Get Your API Key:
- After signing in, navigate to your account settings by clicking on your profile in the top-right corner.
- Select API from the left menu.
- Click Create or Generate to get your API key.

3. Add the API Key to the Project:
- Open the project folder.
- Create a file named .env in the root directory (if it doesn’t already exist).
- Add the following line to the .env file, replacing your_api_key_here with the API key you generated:
```
TMDB_API_KEY = your_api_key_here
```

4. Backup Method (Manual API Key Input):

- If you are unable to use the .env file, the program will prompt you to manually enter the API key during runtime.

5. Run the Project:
- Install all dependencies by running:
```
pip install -r requirements.txt
```
- Run the project. Your .env file will securely load the API key, enabling all API requests to function correctly.

### Follow the instructions below to run the project on your local machine:

1. Clone the Repository -
Navigate to the directory where you want to save the repository using the cd command in your terminal. Then, clone the repository by running the following command:
```
git clone https://github.com/jrhankins883/keanu_whoa_vs_boxoffice
```
2. Navigate to the Cloned Directory -
Change your current directory to the project folder:
```
cd keanu_whoa_vs_boxoffice
```
3. Set Up a Virtual Environment -
It is recommended to use a virtual environment to keep the project dependencies isolated. To create one, run the following command in your terminal:
- On Windows:
```
python -m venv venv
```
- On macOS/Linux
```
python3 -m venv venv
```
This will create a virtual environment named venv in your current directory.

4. Activate the Virtual Environment with the appropriate command for your system:
- On Windows:
```
.\venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```
Your terminal prompt will update to indicate that the virtual environment is active.

5. Install the Required Packages - 
```
pip install -r requirements.txt
```
- If you don't have Jupyter installed, you can install it with:
```
pip install jupyter
```
6. Run the Project -
To execute the Jupyter Notebook file keanu_tmdb.ipynb, follow one of these methods:

- Using Jupyter Notebook:
Enter jupyter notebook in your terminal to launch Jupyter. Then open the keanu_tmdb.ipynb file and run the cells.

- Using Visual Studio Code:
Open the keanu_tmdb.ipynb file in Visual Studio Code. Use the "Run Cell" button at the top left of each cell to execute the code.

7. Deactivate the Virtual Environment
Once you're done, deactivate the virtual environment by typing:
```
deactivate
```
You're all set!

# Graphs/Visualizations and Summary

## Bar and Line Chart - Revenue vs Whoas by Movie
![image](https://github.com/user-attachments/assets/eb1e6219-e074-4438-9234-064330340322)

As you can see, the first few movies of Reeves's filmography either weren't released in theaters or grossed only in the thousands. It's not until *Bill and Ted's Excellent Adventure* that Reeves hits his second highest number of "Whoas" in his entire career. Just a couple years later is the sequel *Bill and Ted's Bogus Journey* and this will be the pinnacle of "Whoas" for the movie star. This graph gives an easy visual representation to the answer we're looking for. Based on this graph, we can surmise that Reeves uttering "whoa" doesn't necessarily lead to big box office numbers. In fact, it's *Toy Story 4* that gives Reeves his biggest success in terms of revenue and he barely utters "whoa" at all. To get the actual numbers, let's move on to the next graph... A scatter plot!

## Scatter Plot of Revenue vs. Total Whoas
![image](https://github.com/user-attachments/assets/84031b10-e8fc-4e75-9573-fb7ef4aa65c7)

The scatter plot is a little harder to glance at and make a conclusion to so I added specifics. Box office revenue and the total number of "whoas" are attached to each movie. With these specifics added in, the scatter plot leaves nothing to the imagination. *Toy Story 4* is Reeves's only $1,000,000,000+ film (which personally surprised me) and he only says "whoa" 1 time! *Bill and Ted's Bogus Journey* takes the crown for the highest number of "whoas" with 28! Audiences may enjoy Reeves's movies, but when he's dropping those "whoas" like crazy, the box office revenue is pretty middle of the road.

![](https://tenor.com/view/coroca-keanu-reeves-gif-19058801.gif)

## Histogram - Distribution of "Whoas" Across Keanu Reeves Movies
![image](https://github.com/user-attachments/assets/a537e2fb-b637-405e-8817-25530989cd54)

I added this graph to give an idea of how often Reeves says "whoa" at all and it turns out that he doesn't say it as often as expected. He says "whoa" less than 5 times in most of the movies where he says the signature word. Ultimately, my conclusion to this little experiment is that a lot of "whoas" have made for some great memes over the years but most of his success seems to stem from movies where he loses the stoner vibe (basically the *Bill and Ted* movies) and plays a hero. Although, I'd argue that Bill and Ted are heroes in their own right!

Maybe home video sales for the *Bill and Ted* movies were high and that's how "whoa" became a part of our pop culture? We can't argue the influence that Reeves has had on moviegoers since the early 90's but I think audiences enjoy watching him play a hero (or love interest) more than watching him play a stoner who says "whoa" a lot. Clearly, based on these graphs, Reeves has left his mark on the world in more ways than one. 

# Code: You Data Analysis Final Project Requirements:
1: Loading Data - Loaded a CSV files:
- A CSV file containing pre-processed 'Whoa' counts per movie.
Used two APIs:
- TMDb API to retrieve Keanu Reeves's filmography and revenue data.
- A secondary API tracking "Whoas" per movie (used for merging and analysis).
- Moved unused CSV files to a backup data folder for proper organization.

2: Clean and Operate the Data While Combining Them:
- Removed unnecessary columns from the API responses.
- Handled missing values, e.g., by filtering out movies with missing revenue data.
- Converted revenue fields from strings to numeric for calculations.

Combined data sets:
- Performed pandas merges to combine API data with CSV data based on movie titles.

Calculated new values:
- Created a "Total Whoas in Movie" field from one data set.

Performed basic text analysis (natural language processing):
- Extracted the most common words from movie titles for exploratory analysis.

3: Visualize/Present Your Data:
- Created three matplotlib visualizations:
- A scatter plot comparing movie revenue to the total number of "Whoas" with annotations for key data points.
- A histogram showing the distribution of movie revenues.
- A bar chart with a line plot overlay comparing revenue and "Whoas" per movie.
- Uploaded static images of all three graphs to the repository for accessibility.
- Annotated visualizations with clear titles, axis labels, and legends to enhance clarity.

4: Best Practices:
- Utilized a virtual environment to keep project dependencies isolated.
- Created a .gitignore file to exclude sensitive information (e.g., .env file for API keys and venv directory).
- Listed all dependencies in a requirements.txt file for easy replication.
- Provided step-by-step setup instructions in the README.md, including how to install Python, Git, and the project's dependencies.

5: Interpretation of Data
- Included markdown cells in the Jupyter Notebook to explain each step.
- Added detailed comments in the code to describe its functionality.
- Created a well-structured README.md:
- Provided a summary of the project, setup instructions, and descriptions of the visualizations.
- Analyzed trends, such as whether more "Whoas" correlate with higher box office revenue.
- Shared insights into Keanu Reeves's filmography and its impact.


![](https://tenor.com/view/thank-you-thanks-gif-19684718.gif)
