import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import ProjectToDoList from "./components/ProjectToDo";
import LoginForm from "./components/Auth";

import axios from "axios";
import Cookies from "universal-cookie";
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
            'todos': [],
            'token': ''

        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
                                                                      password: password})
            .then(response => {this.set_token(response.data['token'])})
            .catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        // отображение списка пользователей
        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                // const users = response.data
                this.setState({'users': response.data['results']})
            }).catch(error => {console.log(error)
               this.setState({'users': []})
            })

        // отображение списка проектов
        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                // const projects = response.data
                this.setState({'projects': response.data['results']})
            }).catch(error => {console.log(error)
               this.setState({'projects': []})
            })

        // отображение списка заметок
        axios.get('http://127.0.0.1:8000/api/todo', {headers})
            .then(response => {
                //const todos = response.data
                this.setState({'todo': response.data['results']})
            }).catch(error => {console.log(error)
               this.setState({'todos': []})
            })
    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            <li>
                                {this.is_authenticated()
                                    ? <button onClick={() => this.logout()}>Выйти</button>
                                    : <Link to='/login'>Войти</Link>}
                            </li>
                        </ul>
                    </nav>
                    <hr/>
                    <Switch>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                        <Route exact path='/projects/:project_name' component={() => <ProjectToDoList projects={this.state.projects}/>}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) =>
                                                                     this.get_token(username, password)}/>}/>
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
