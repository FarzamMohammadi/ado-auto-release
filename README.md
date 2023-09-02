# ADO Express 🚀
![GitHub release](https://img.shields.io/github/v/release/FarzamMohammadi/ado-express)
![GitHub](https://img.shields.io/github/license/FarzamMohammadi/ado-express)

Welcome to the ADO Express codebase, your new go-to tool for release management. This application is crafted to simplify and enhance the Azure DevOps release deployment process. It's intuitive, efficient, and powerful; ADO Express will revolutionize the way you handle releases.

## Quick Start

You have two options to get started:

1. **CLI Tools**: Run tasks quickly without any fuss. You can execute the CLI with either Docker or Python installed on your machine. For more details, refer to [CLI Usage](#%EF%B8%8F-cli-usage).
   
2. **Web Application**: For those who prefer a more graphical approach with an intuitive user interface, you can opt for the full web application. For this option, proceed to [Web Application Usage](#%EF%B8%8F-web-application-usage).

---

## ✨ UI Preview

![Alt Text](./media/ui-preview.gif)

# 🖥️ CLI Usage

Run various tasks through the CLI with minimal setup. You can either use Docker or have Python installed. Not only will your results be logged, but they will also be saved into an Excel file located in [deployment-plan](ado_express\files\search-results\deployment-plan.xlsx).

1. [Docker Deployment](#docker-deployment)
2. [Docker Development Container](#docker-development-container)
3. [Other methods](#additional-cli-options)

## Docker Deployment

1. **Prerequisite**: Ensure Docker is running.
2. **Build Container**: Navigate to the repository directory and execute the following command:
    ```sh
    docker build -t <CONTAINER_NAME> .
    ```
3. **Environment Variables**: Configure the required environment variables in the [.env](/.env) file.
4. **Run Container**: Execute the following command from within the repository directory:
    ```sh
    docker run --env-file ./.env -it <CONTAINER_NAME>
    ```

## Docker Development Container

1. **Prerequisite**: Ensure Docker is running.
2. **VS Code Setup**: Open the repository directory in Visual Studio Code.
3. **Environment Variables**: Update your [.env](/.env) file with necessary variables.
4. **Quick Start**: Press `F1`, then search for and select `Dev Containers: Rebuild and Reopen in Container`.

## Additional CLI Options

For comprehensive CLI options, navigate to the dedicated README in the `./ado_express` directory. 

Quick Access: [CLI README](./ado_express/README.md)

Discover various instructions, tips, and tricks for optimizing your CLI experience!

# 🖥️ Web Application Usage

To operate the ADO Express Web Application, you must start both the [Frontend](#-frontend) and [Backend](#-backend-api) services of this project.

## 🎨 Frontend

The frontend of ADO Express is a sleek and modern web application. Let's get it running:

1. Navigate into the frontend directory:
   ```sh
   cd ado_express_app
   ```
2. Install Dependencies:
   ```sh
   npm i
   ```
4. Run the development server:
   ```sh
   npm run start
   ```
   Voila! You should now have the ADO Express web application running locally.

## 🔧 Backend (API)

The backend (API) of ADO Express powers all of the magic behind the scenes. To get it running, follow these steps:

### Preparation

First, you need to set up a virtual environment and install the necessary dependencies:

1. Create a virtual environment:
   ```sh
   python -m venv ./venv
   ```
2. Activate the virtual environment:
   - Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```sh
     source venv/bin/activate
     ```
3. Install Dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Run the API

With the virtual environment set up, you can now run the API:

1. Navigate into the API directory:
   ```sh
   cd ado_express_api
   ```
2. Start the application:
   ```sh
   daphne asgi:application
   ```

That's it! You should now have the ADO Express API running locally.

## 🌟 Shine Bright

ADO Express is more than just a tool; it's a game changer. With an emphasis on usability and performance, this app aims to simplify the complexities of release management, allowing you to focus on what truly matters - creating outstanding software.

Feel free to explore the repository, try out the application, and even contribute. Enjoy your journey with ADO Express!

## 🎥 See It To Believe It: The ADO Express Demo

Ever wondered how 'seamless' and 'efficient' looks in action? Well, wonder no more! [Click here to witness ADO Express revolutionizing Azure DevOps release management right before your eyes!](https://www.linkedin.com/posts/farzam-m_warmest-greetings-everyone-time-does-indeed-activity-7083582850511372288-Ov6c?utm_source=share&utm_medium=member_desktop) Experience the UI, functionality, and the game-changing features that will redefine your approach to release management. Don't just take our word for it—see it for yourself!

## 💡 Features

ADO Express boasts a range of features to simplify your Azure DevOps release management process. Here are some of the highlights:

- **Automated Release Management**: ADO Express automates your entire release management process, saving you time and ensuring uniformity in all your deployments. It prevents unwanted releases in deployments, and takes you from start to finish in your Continuous Deployment pipeline.

- **Search and Export**: With ADO Express, you can easily search through your releases and export your results to an Excel file. Whether you're using an ADO query or a deployment plan Excel file, ADO Express provides you with a detailed log of your release deployments.

- **Detailed Release Deployment**: ADO Express offers three types of detailed deployments: via query, via release number, and via environment. Each deployment type comes with its unique advantages, giving you the flexibility to choose the deployment method that best suits your needs.

- **Crucial Release Deployment Management**: ADO Express lets you mark certain releases as 'crucial.' These crucial deployments are run first, and in case of a deployment error, the application attempts to rollback and stop the processes.

- **Easy Run Options**: ADO Express provides you with a variety of ways to run the tool, from Docker to local execution, giving you the flexibility to choose the method that fits best in your workflow.

- _And many more..._: Dive in and discover what ADO Express has in store!

## 🛠️ Built With

ADO Express utilizes a robust tech stack:

- Frontend: **Svelte**, **Typescript**, **Tailwind**
- Backend: **Python**, **Django**

## 🤝 Contributions & Feedback

While we don't currently have a formal contribution guide, we still warmly welcome contributions from all! If you have suggestions, bug reports, or want to contribute code, please feel free to open an issue or pull request on our GitHub repository.

Also, if you encounter any issues or have ideas for enhancements, we would love to hear from you! Just head over to the [ADO Express Issues](https://github.com/FarzamMohammadi/ado-express/issues) page and drop us a note.

Whether you're providing feedback, reporting issues, or contributing to the code, your involvement is what makes this project shine. Thanks for being a part of ADO Express!

## 📝 License

This project is licensed under the terms of the [MIT license](LICENSE).

## 📮 Get in Touch

Have questions, suggestions, or just want to chat about ADO Express? Reach out!

- Farzam Mohammadi: [Email](mailto:farzammohammadia@gmail.com)
