# MealPlanner
MealPlanner is a meal planning app created using Flask. The main purpose is to practice Flask development and to get more comfortable with other libraries/technologies like WTForms and MySQL.

The basis of the web app is from Traversy Media's [Flask from Scratch series](https://www.youtube.com/watch?v=zRwy8gtgJ1A). I followed along in that tutorial to create the project in another one of [my Flask repos](https://github.com/ColtanF/FlaskTutorialCode). This MealPlanner app takes the bones of that project and does something similar but different.

## Current Functionality

Currently, the MealPlanner web app will allow a user to view the Home and About screens (not much going on there yet), browse existing meals, and add their own custom meals. Meal information is now stored in a MySQL DB.

## Planned Functionality

There are several menu items that are currently not in use. In the Tools menu, the Generate and Goals items currently do nothing, as do the Register/Login links.

The Generate menu item will allow the user to input some parameters for the type of meal they want to eat, and the app will return a random meal meeting the user's requirements. This will be useful when a user knows they want to eat something with a certain amount of calories, or protein, or carbs, but can't decide exactly what they want to eat. Eventually, this will be expanded to generate an entire day's worth of meals.

The Goals menu item will allow the user to input some data about themselves and what goals they want to achieve (for example, gain or lose some amount of weight), and the app will do some calculations to return some information to the user to help them meet their goals. For example, the user could input their height and weight, and then specify that they want to lose 10 pounds in two months. The app could then return information about the user's current sustainment caloric intake, how many calories they burn in a day, and how many calories they should consume to lose the weight they want to lose.

As for the Register/Login links, I think it would be a good idea for users to have to be logged in to add more meals to the database, or to have meals in the database registered to specific users so that those specific meals are used in the generation of their random meals.

There are other pieces of functionality I'd like to add in the future (adding specific ingredients as their own data objects vs. as part of meals, choosing ingredients from a list instead of just typing them into a text box, etc.), but the above items are the basic functionality I'd like to build.