import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td><Link to={`projects/${project.project_name}`}>{project.project_name}</Link></td>
            <td>{project.repo_link}</td>
            <td>{project.users_of_project}</td>
            <td><button onClick={() => deleteProject(project.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
            <table>
                <tbody>
                    <tr bgcolor='#D3D3D3'>
                        <th>PROJECTS NAME</th>
                        <th>LINKS</th>
                        <th>USERS</th>
                        <th></th>
                    </tr>
                    {projects.map((project) => <ProjectItem project={project}
                                                            deleteProject={deleteProject}/>)}
                </tbody>
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList;
