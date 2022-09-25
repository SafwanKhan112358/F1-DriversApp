# F1_2022_Drivers_App
An app that lets users search a driver, and receive all-time statistics for the driver and relevant stats for the current season

- App is made using Python, Tkinter, and requests(HTTP library)
- Data is generated through a public F1 API, Ergast Developer API
- Used Postman API + API documentation to generate request links

Pictures of App: 

Core: 
![image](https://user-images.githubusercontent.com/62441768/192161265-d424021d-11fb-4065-aea6-d2d0af031cb7.png)

Start-of-app:
![start of app](https://user-images.githubusercontent.com/62441768/192161327-c49ca8be-55d6-46be-bb62-ea489a0c905f.png)

Listbox search functionality
![listbox search-functionality](https://user-images.githubusercontent.com/62441768/192161294-3c733215-5948-41b2-ad50-e8c1e9041d27.png)



Front-End Features: 

- app is divided into 2 frames, a searching frame and a content frame
- entrybox to let users type text
- dynamic listbox which is connected to entrybox, giving suggestions based on live user input
- Alternatively to typing entire names, users can write a few letters and then pick suggested items from listbox. Selection appears in entry-box, and listbox is hidden simultaneously
- After writinng/selecting driver name, user can search it
- through a lambda function, search button is binded to the enter button on keyboard, so users can either press enter to activate the search button, or can directly press on it


API Functionality: 

- user-input is validated and converted to an id that's passed to several api functions, making GET requests (using the id) to an api, and display the generated content

Error and Exception Handling:
- can handle invalid inputs, by returning a message (appears temporarily) stating that the input doesn't exist
![image](https://user-images.githubusercontent.com/62441768/192162602-21b09094-6477-435c-b328-7cde44a27423.png)







  

