

const startProject = document.getElementById("start_project")
const newProject = document.querySelector(".new-project")
const showProjectForm = () => {
    newProject.style.display = 'block'
    startProject.parentElement.parentElement.style.display = 'none'
}

startProject.addEventListener("click", showProjectForm)