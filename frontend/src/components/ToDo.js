import React from "react";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.note_text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.user}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <tbody>
                <tr bgcolor='#D3D3D3'>
                    <th>PROJECT</th>
                    <th>NOTES</th>
                    <th>CREATED</th>
                    <th>UPDATED</th>
                    <th>USERS</th>
                    <th>ACTIVE</th>
                </tr>
                {todos.map((todo) => <ToDoItem todo={todo}/>)}
            </tbody>
        </table>
    )
}

export default ToDoList;