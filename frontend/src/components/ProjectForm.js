import React from 'react'

class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {project_name: '', users_of_project: props.users_of_project}
    }

    handleChange(event) {
        this.setState(

            {
                [event.target.name]: event.target.value
            }
        );
        // console.log(this.state)
        // console.log(event.target.name, event.target.value)
    }

    handleSubmit(event) {
        // console.log(this.state.users_of_project)
        this.props.createProject(this.state.project_name, this.state.users_of_project)

        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="project_name">Project name</label>
                    <input type="text" className="form-control" name="project_name"
                           value={this.state.project_name} onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="user_of_project">Users of project</label>
                    {/*<input type="text" className="form-control" name="users"*/}
                    {/*       value={this.state.user} onChange={(event) => this.handleChange(event)}/>*/}
                    <select name="users_of_project" className='form-control' onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((item)=><option value={item.uid}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm