# About

The Faculty Advising System is a system developed using React.js as the frontend framework and Django as the backend framework for NSU official work purposes. Firebase stores data in a real-time database, and Firebase Authentication is implemented for login and sign-up functionality.

## Project Details

This system was designed for the NSU ECE department under the supervision of faculty member Nova Ahmed. The main objective was to automate and simplify the advising system for faculty advisors in the NSU ECE department. The project included all faculties within the ECE department.

## Key Features:

- **Frontend Framework: React.js**: The frontend framework, React.js, provides a robust and user-friendly interface for faculties and the admin. Its modular architecture allows for efficient development and easy maintenance of the system's components. The use of React.js ensures a smooth and responsive user experience.

- **Backend Framework: Django**: Django, the backend framework, empowers the system with a scalable and secure foundation. It follows the Model-View-Controller (MVC) architectural pattern, enabling efficient data management and seamless integration with the frontend. Django's built-in authentication and authorization mechanisms ensure that only authenticated users can access the system, enhancing security.

- **Database: Firebase Realtime Database**: Firebase Realtime Database is a NoSQL cloud-based database that offers real-time synchronization and offline capabilities. By leveraging Firebase, the system achieves efficient data storage and retrieval, ensuring that the faculty requests and other relevant information are instantly accessible to the admin and faculties.

- **Authentication: Firebase Authentication**: The Firebase Authentication feature provides a secure login and sign-up process for faculties. It supports various authentication methods, such as email and password, ensuring that only authorized individuals can access the system's features and resources. Firebase Authentication handles the authentication process seamlessly, freeing up development time for other critical aspects of the system.

- **Email Notifications**: The system's email notification functionality plays a crucial role in keeping all stakeholders informed. The admin receives automated email notifications with faculty information when new course requests are submitted. Additionally, when multiple faculties express interest in the same course section, email alerts are sent to notify them. These notifications facilitate effective communication and coordination between the admin and faculties.

- **Automation Feature**: The automation feature within the system significantly reduces manual effort and improves efficiency. By automating the assignment of course sections and faculty names, the admin can allocate resources effectively and expedite the course scheduling process. This automation capability not only saves time but also ensures fairness and adherence to departmental rules by utilizing a senior to junior faculty order.

- **Table-Form View**: The system's ability to generate a comprehensive table-form view of the filled-up forms simplifies the admin's task of reviewing and managing faculty requests. The admin can easily navigate through the table, make necessary edits, and sort the data according to course names, ensuring smooth coordination and organization of the advising process.

- **Flexibility and Edits**: The system's flexibility allows the admin to make adjustments as needed. If any mistakes or changes are identified in the submitted table, the admin can edit specific fields to rectify the errors. This ability to modify and update information ensures accuracy and keeps the advising process aligned with the faculties' requirements.

- **Data Submission and Storage**: The final submission of the course scheduling data marks an important milestone in the process. After the admin submits the data, it is securely stored in the database for future reference and retrieval. The table results displayed on the 'table-admin' page provide a comprehensive overview of the assigned course sections, facilitating efficient management and tracking of the advising process.

By incorporating these additional descriptions, the explanation provides a more comprehensive and detailed understanding of the system's features and their significance within the context of faculty advising in the NSU ECE department.

# Workflow

## Login and Course Request Process

The system provides a login feature for faculties to access their accounts using faculty initials and RDS passwords. After logging in, faculties can fill out a form on a dedicated webpage to request courses for the upcoming semester. The submitted forms are saved in the database, and the admin is notified via email with faculty information. The email notifications can be customized by the admin.

## Admin Management Capabilities

The admin can log in and view a 'table-form' that lists all the filled forms submitted by faculties. The admin has the authority to set the time and section for each course based on faculty requests, following department rules. When multiple faculties request the same section, the admin can use an automation feature to streamline the process.

## Streamlined Automation Process

If multiple faculties express interest in the same course section, the system sends email notifications to inform the faculties. The faculties fill out a form with available course choices, which are stored in the database. The admin can review this list from the 'table-request' page. The admin fills out the timeset form on the 'timeset' page to set the final timing schedule. Faculty initials are assigned randomly from the requested table for courses, ensuring compliance with department rules. In case of multiple faculties are assigned to the same course section, an alert is sent to the admin. The admin adds a 'SENIOR TO JUNIOR.txt' file listing faculty names in senior to junior order. Clicking the 'auto' button triggers the automation process, populating faculty initials on the timeset page according to section and seniority. This automation feature simplifies the admin's work and improves efficiency. After completing the automation, the admin submits the data, which is saved in the database. The table results are displayed on the 'table-admin' page, where the admin can further automate and sort the list according to course names.

## Additional Features and Flexibility

The admin has the ability to edit specific fields in the submitted table if any mistakes are identified. Faculties can access their respective pages after logging in, where their assigned timings are displayed.

# License

[MIT License](LICENSE)

The Faculty Advising System is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

