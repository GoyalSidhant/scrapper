Develope a Python CLI Application with the following utilities
 
1. Make a scraper which fills the form at https://parivahan.gov.in/rcdlstatus/?pur_cd=101 and scrapes the resultant data.
2. Use the Python library requests, lxml along with xpath to do so.
3. The page contains a Captcha so write a dummy function get_captcha() which outputs the text of captcha based on the input image of the captcha, assume that the captcha can be wrong sometimes, so handle retries accordingly. For testing purposes, you can use the Python input function to enter captchas manually while scrapping, but you will be judged after we replace it with our get_captcha() and run tests on thousands of samples, so make sure to make this scrapper fault tolerant and output useful error messages.
 
Here is a sample page of the result after filling the form - https://imagebin.ca/v/4eE1iM6REVNM
 
Here is a sample Driving License to try out - https://5.imimg.com/data5/UD/GT/MY-35587652/driving-license-service-500x500.jpg
 
The result should have all the fields like Name, Date of Issue, Date of expiry, Class of Vehicles etc.
 
The final application should demand a Driving License Number and Date of Birth, and should shell out the results in JSON format.