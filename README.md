# BA505 Final Project
## Team Fire

## Files in our repositories
- Final Notebook
- fcounty_clean.csv - This is our dataset
- Import.py - This is our file for reading the dataset

## Introduction 
For our final project we decided to look at Fire Incident data for Connecticut in 2014.  We found this information from the following source: https://data.ct.gov/Public-Safety/Connecticut-Fire-Department-Incidents-2014/axrk-twst . The dataset was too large to push to GitHub. Therefore, we considered which sampling method would be best to reduce the size of our data. We utilized stratified sampling to select towns within Fairfield County to obtain a sample population that best represents the entire population being studied. The selected towns were: Fairfield, Greenwich, Norwalk, Stamford, Westport, Darien, Noroton Heights, Noroton, Rowayton.


## Data Analysis Tools
We used the standard imports as well as the Scikit Learn regression tool. 

## Data Cleaning
We deleted columns we considered irrelavent for our study. Then, we created new columns that allowed us to analysis the data in a meaningful way. 


## Data Analysis
We began with statistical plots on all the data in the dataset to get a better understanding of the information. Next we looked at towns in the Fairfield county area. Finally we looked at the the performance of the Fairfield Fire Department. 

## Conclusion
- There is more incidents in January than any other month.
- Most incidents occur between 11:00 a.m. - 12:00 p.m.
- The average operation duration increases across the year.
- Fairfield has the most incidents vs. population.
- EMS calls were the most frequent type.
- Building fires amassed the greatest total loss amount.
These were some of our conclusions based on looking at the 2014 Connecticut Fire department data. We were able to answer most of the questions we hoped to at the beginning of the study. It would be interesting to look at other yearly data for Connecticut to test our results across different years. Also if we had a way of differencing the fire departments in each town and the type of fire department, it would be nice to compare performance across the fire departments.
