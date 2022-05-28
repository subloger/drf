import React from "react";
import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.repo_link}</td>
            <td>{project.users_of_project}</td>
        </tr>
    )
}

const ProjectToDoList = ({projects}) => {
    let { project_name } = useParams();
    let filtered_project = projects.filter((project) => project.project_name === project_name)
    return (
        <table>
            <tr bgcolor='#D3D3D3'>
                <td>PROJECTS NAME</td>
                <td>LINKS</td>
                <td>USERS</td>
            </tr>
            {filtered_project.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectToDoList;
