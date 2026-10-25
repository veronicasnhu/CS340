# CS340

This repository contains my CS 340 Project Two work, including the MongoDB database connection, reusable Python CRUD module, and interactive Dash dashboard created for Grazioso Salvare.

## How do you write programs that are maintainable, readable, and adaptable?

I try to keep programs maintainable and readable by keeping different parts of the program separate instead of putting everything in one place. In this course, the CRUD Python module handled the connection to MongoDB and the Create, Read, Update, and Delete operations. I was then able to reuse that module in Project Two to connect the dashboard to the database without having to rewrite the same connection and query code throughout the dashboard.

This made the project easier to work with because the database code stayed in one reusable module while the dashboard focused on displaying and filtering the data. In the future, I could use a similar CRUD module for other applications that connect to MongoDB, such as inventory systems, customer databases, or other dashboards.

## How do you approach a problem as a computer scientist?

I approached this project by breaking the requirements into smaller parts and testing each part as I worked. I first made sure the database connection and CRUD module worked, then moved on to the data table, rescue filters, pie chart, and geolocation map. Testing as I went helped me catch problems like the logo file path, filter results, and chart layout before moving on.

This project was different from some of my previous assignments because I had to get several parts of the application working together. I had to think about the database, Python code, queries, and dashboard instead of focusing on just one part. I also had to compare the requirements with the actual data. For example, some breed names included values such as German Shepherd Mix instead of only German Shepherd, so I adjusted the queries to account for that.

In future projects, I would keep using the same approach of breaking requirements into smaller tasks, looking at the data before writing queries, and testing each feature as I build it.

## What do computer scientists do, and why does it matter?

Computer scientists use technology to solve problems and make information easier for people to use. This can include organizing data, creating databases, writing software, and building tools that make tasks easier or faster.

For Grazioso Salvare, the dashboard makes the animal shelter data easier to access and understand. Instead of manually searching through the MongoDB database, the user can select a rescue type and see matching animals in the data table, pie chart, and geolocation map. This helps Grazioso Salvare find animals that match what they are looking for more quickly and makes the database easier to use.
