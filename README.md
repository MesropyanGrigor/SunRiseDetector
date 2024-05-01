**Task**

Your task is to write a script that uses the Sunrise and Sunset API to determine the closest date when the sunrise in Paris will occur at 6:00 AM. The script should output this date in a human-readable format.
API Information:
You’ll be working with the following endpoint: https://api.sunrisesunset.io/json
Your script must correctly utilize this API, incorporating necessary parameters to target sunrise times specifically for Paris.


**Recruiter Solution Checklist**

- Accuracy of the Date: Does the script correctly identify May 23, 2024, as the closest date when sunrise in Paris will be at 6:00 AM?
- Comprehensive Error Handling: Are there checks for common errors such as network issues, invalid API responses, and data parsing errors?
- Graceful Failure: Does the script fail gracefully, providing clear error messages without crashing or hanging?
- Originality vs. Borrowing Code: Has the candidate created the solution independently or adapted from external sources like Stack Overflow? Were chunks of the code borrowed from the external sources?
- Functionality: Does the solution work as intended without manual intervention to correct errors or provide missing information?
- Hardcoding vs. Dynamic Input: Are parameters (such as the date range, coordinates for Paris, or time of sunrise) hardcoded, or does the script allow for dynamic inputting of these values?
- Evidence of Testing: Has the candidate provided any form of testing or validation to ensure their script works as expected?
- Discussion of Potential Issues: Is there a discussion or comments in the code about potential pitfalls or what could go wrong with the script’s approach?
- Clarity of Comments: Are the comments in the code clear, helpful, and informative about the logic and flow of the script?
- Documentation of Assumptions: Has the candidate documented any assumptions made during the development of their solution?
- Code Organization: Is the code well-organized, structured, and easy for someone with basic Python knowledge to follow?
- Handling API Changes: Is there any consideration or mention of how the solution might adapt to potential changes in the API’s structure or response format?
- Clarity of Variable Names: Are variable names intuitive and clear, making the code easier to understand even for someone without a deep programming background?


#### **Dependencies**
- httpx

#### Run example of the program
```commandline
python3 ./run.py --country Paris --sun_rise_time "6:00 AM"
```