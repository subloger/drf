import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import ProjectToDoList from "./components/ProjectToDo";
import axios from "axios";
import {Route, Link, Switch, Redirect, BrowserRouter} from "react-router-dom";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу `{location.pathname}` не найдена</h1>
        </div>
    )
}

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': []

        }
    }

    componentDidMount() {
        // отображение списка пользователей
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users.results
                    }
                )
            }).catch(error => console.log(error))

        // отображение списка проектов
        axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects.results
                    }
                )
            }).catch(error => console.log(error))

        // отображение списка заметок
        axios.get('http://127.0.0.1:8000/api/todo')
            .then(response => {
                const todos = response.data
                console.log(todos)
                this.setState(
                    {
                        'todo': todos.results
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todo'>ToDo</Link>
                            </li>
                        </ul>
                    </nav>
                    <hr/>
                    <Switch>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                        <Route exact path='/projects/:project_name' component={() => <ProjectToDoList projects={this.state.projects}/>}/>
                        <Redirect from='/' to='projects'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <hr/>
            </div>
        )
    }
}

export default App;
