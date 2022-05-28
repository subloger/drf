import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td><Link to={`projects/${project.project_name}`}>{project.project_name}</Link></td>
            <td>{project.repo_link}</td>
            <td>{project.users_of_project}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <tbody>
                <tr bgcolor='#D3D3D3'>
                    <th>PROJECTS NAME</th>
                    <th>LINKS</th>
                    <th>USERS</th>
                </tr>
                {projects.map((project) => <ProjectItem project={project}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList;
